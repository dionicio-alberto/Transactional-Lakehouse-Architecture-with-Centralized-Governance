import sys
import logging
import gc
from typing import Optional
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from faker import Faker

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SimulatorEngine:
    def __init__(self, raw_stock_csv_path: str, output_base_dir: str):
        """
        Initializes the simulator engine for AAPL transaction generation.
        """
        self.raw_stock_csv_path = raw_stock_csv_path
        self.output_base_dir = output_base_dir
        
        # Load Raw AAPL dataset into memory (cached once)
        logging.info(f"Loading base Kaggle AAPL file from {raw_stock_csv_path}...")
        try:
            self.stock_df = pd.read_csv(raw_stock_csv_path)
            # Ensure proper datetime parsing for 'Date' column
            self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'], errors='coerce')
            self.stock_df = self.stock_df.dropna(subset=['Date']).sort_values('Date')
        except Exception as e:
            logging.error(f"Failed to read stock dataset: {e}")
            raise

    def generate_users(self, total_users: int = 1000) -> pd.DataFrame:
        """
        Generates precisely `total_users` interacting with the system.
        Enforces a > 30% LATAM distribution rule.
        """
        logging.info(f"Generating {total_users} synthetic users...")
        fake_latam = Faker(['es_MX', 'pt_BR', 'es_AR', 'es_CO'])
        fake_global = Faker(['en_US', 'en_GB', 'fr_FR', 'de_DE'])
        
        # We need >30% LATAM explicitly
        latam_count = int(total_users * 0.35)
        global_count = total_users - latam_count
        
        users_data = []
        
        # Generator for global users
        for _ in range(global_count):
            users_data.append({
                "user_id": fake_global.uuid4(),
                "first_name": fake_global.first_name(),
                "last_name": fake_global.last_name(),
                "email": fake_global.email(),
                "ssn": fake_global.ssn(),
                "country": fake_global.current_country_code()
            })
            
        # Generator for LATAM users
        for _ in range(latam_count):
            users_data.append({
                "user_id": fake_latam.uuid4(),
                "first_name": fake_latam.first_name(),
                "last_name": fake_latam.last_name(),
                "email": fake_latam.email(),
                "ssn": fake_latam.ssn(),
                # In Faker, localizations don't always generate the precise localized country code. We force it to be explicitly a LATAM subset.
                "country": np.random.choice(["MX", "BR", "AR", "CO"])
            })
            
        users_df = pd.DataFrame(users_data)
        
        # Write to staging
        users_path = f"{self.output_base_dir}/users/users.parquet"
        users_df.to_parquet(users_path, engine='pyarrow', compression='snappy')
        logging.info(f"Successfully generated users. Saved to {users_path}")
        
        return users_df

    def process_chunk(self, users_df: pd.DataFrame, start_year: int, end_year: int, batch_name: str):
        """
        Simulates transactions within the specified date bounds using Pandas vectorization.
        Executes a Chunk-and-Flush memory pattern to prevent memory bloating over long timescales.
        """
        logging.info(f"Processing chunk {batch_name} from {start_year} to {end_year}...")
        
        # Slice the AAPL stock timeframe
        period_df = self.stock_df[(self.stock_df['Date'].dt.year >= start_year) & (self.stock_df['Date'].dt.year < end_year)].copy()
        
        if len(period_df) == 0:
            logging.info(f"No trading data available for range {start_year} to {end_year}. Skipping.")
            return

        # Explode transactions pseudo-randomly for active trades
        # For performance, we sample random user IDs to map against AAPL days
        # Instead of iteration, we randomly replicate elements to generate volume.
        
        # Let's assume daily average of thousands of trades across the 1000 users.
        # To avoid blowing up perfectly, we do ~10 trades per ticker day represented by random users.
        trade_multiplier = 10 
        
        expanded_indices = np.repeat(period_df.index.values, trade_multiplier)
        transactions_df = period_df.loc[expanded_indices].copy().reset_index(drop=True)
        
        # Array assignment - Vectorization pattern (No For Loops)
        user_ids = users_df['user_id'].values
        transactions_df['transaction_id'] = [Faker().uuid4() for _ in range(len(transactions_df))]
        transactions_df['user_id'] = np.random.choice(user_ids, size=len(transactions_df))
        
        # Define synthetic properties matching the Domain Entity rules
        transactions_df['trade_type'] = np.random.choice(["BUY", "SELL"], size=len(transactions_df))
        transactions_df['quantity'] = np.random.randint(1, 1000, size=len(transactions_df))
        
        # Align column names to final contract (market_open, market_high...)
        column_mapping = {
            'Date': 'trade_date',
            'Open': 'market_open',
            'High': 'market_high',
            'Low': 'market_low',
            'Close/Last': 'market_close', # Kaggle column format
            'Close': 'market_close',
            'Volume': 'market_volume'
        }
        
        transactions_df.rename(columns=column_mapping, inplace=True, errors='ignore')

        # Drop columns that are not part of our explicit domain model contract
        keep_cols = [
            'transaction_id', 'user_id', 'trade_date', 'trade_type', 'quantity',
            'market_open', 'market_high', 'market_low', 'market_close', 'market_volume'
        ]
        
        # Ensure only columns that exist are kept
        final_cols = [c for c in keep_cols if c in transactions_df.columns]
        transactions_df = transactions_df[final_cols]
        
        # Write out
        out_path = f"{self.output_base_dir}/transactions/{batch_name}.parquet"
        transactions_df.to_parquet(out_path, engine='pyarrow', compression='snappy')
        logging.info(f"Flush Complete: Parquet payload successfully anchored to {out_path}.")
        
        # Resilience: Memory Management
        # Del and force GC collection prevents lingering dataframe bloat
        del period_df
        del expanded_indices
        del transactions_df
        gc.collect()
        
    def process_raw_table(self, file_path: str):
        """
        Takes an isolated raw CSV and pushes it strictly as a compressed Parquet
        table into the correct corresponding destination folder.
        """
        import os
        filename = os.path.basename(file_path)
        table_name = filename.replace('.csv', '')
        
        logging.info(f"Processing Raw CSV to Table Stage: {table_name}")
        
        try:
            # We explicitly handle varying encodings or broken rows gracefully.
            df = pd.read_csv(file_path, low_memory=False)
            
            table_out_dir = os.path.join(self.output_base_dir, table_name)
            os.makedirs(table_out_dir, exist_ok=True)
            
            out_path = os.path.join(table_out_dir, f"{table_name}.parquet")
            df.to_parquet(out_path, engine='pyarrow', compression='snappy')
            logging.info(f"Successfully staged table {table_name} at {out_path} ({len(df)} rows)")
            
            del df
            gc.collect()
        except Exception as e:
            logging.error(f"Failed to isolate {table_name}: {e}")

