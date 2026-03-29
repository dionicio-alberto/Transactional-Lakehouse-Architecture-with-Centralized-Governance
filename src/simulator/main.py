import os
import sys
import logging
import glob
from generator import SimulatorEngine

# Ensure output paths exist
STAGED_BASE_DIR = os.path.join(os.path.dirname(__file__), "data/staged")
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data/raw")
PRIMARY_STOCK_CSV = os.path.join(RAW_DATA_DIR, "aapl_historical_data.csv")

def main():
    logging.info("Starting Simulator Initialization Phase...")
    
    # Using relative paths for decoupling, falling back gracefully
    if not os.path.exists(PRIMARY_STOCK_CSV):
        logging.error(f"Cannot find primary Kaggle RAW data at {PRIMARY_STOCK_CSV}")
        sys.exit(1)
        
    engine = SimulatorEngine(
        raw_stock_csv_path=PRIMARY_STOCK_CSV,
        output_base_dir=STAGED_BASE_DIR
    )
    
    # 0. Batch process all raw Kaggle Tables to Lakehouse native Parquet
    logging.info("Initiating Raw to Staged bulk conversion...")
    for file_path in glob.glob(os.path.join(RAW_DATA_DIR, "*.csv")):
        engine.process_raw_table(file_path)
    
    # Pre-generate persistent users domain map
    users_df = engine.generate_users(total_users=1000)
    
    # 1. Chunk and bulk load the first 20 years natively (1980 - 2000)
    engine.process_chunk(
        users_df=users_df, 
        start_year=1980, 
        end_year=2000, 
        batch_name="batch_initial_20_years"
    )
    
    # 2. Incrementally simulate yearly bulk inserts replicating modern day
    # Loop across 2000 to 2026 generating a new parquet dataset per partition year
    # Each loop cycle invokes `gc.collect()` at the end of the generator process inside the class.
    for year in range(2000, 2027):
        engine.process_chunk(
            users_df=users_df, 
            start_year=year, 
            end_year=year + 1, 
            batch_name=f"batch_{year}"
        )
        
    logging.info("Simulation Completely Finished. Process exiting gracefully.")

if __name__ == "__main__":
    main()
