# Unit 1: Business Logic Model

## 1. Overview

The Data Simulator mimics a financial institution processing users and stock transactions (Apple symbol AAPL) to simulate a long-running data environment.

## 2. Core Workflows

### 2.1 Synthetic PII Generation Process

- The simulator initializes the `Faker` library.
- It generates precisely **1,000 distinct user records**.
- Each user is assigned random PII such as Name, SSN, and Email.
- The geography rules dictate specific probability distributions for user countries.

### 2.2 Transaction Aggregation Process

- The system ingests the raw Kaggle Apple Stock Dataset.
- Each row in the stock dataset represents a trading day (Date, Open, High, Low, Close, Volume).
- For each trading day, the system distributes simulated trades among the generated users.

### 2.3 Incremental Batch Simulation

- **Initial Load Phase**: The first 20 years of Apple stock data (e.g., 1980 to 2000) are compiled into a massive historical bulk chunk representing "legacy" data.
- **Incremental Phase**: The subsequent 20+ years of data are split on a yearly basis. Each year becomes a distinct `charge` or batch simulating a scheduled ETL run.
- **Output Workflow**: The script exports every batch as a distinctly named compressed **Parquet** file within a partitioned bucket structure in the `raw-zone`.
