# Functional Design Plan - Unit 1 (Python Data Simulator)

## Objective
Design the detailed business logic, domain models, and business rules for the Python Data Simulator module. This module is responsible for generating incremental batches of user PII and combining it with Kaggle Apple Stock data.

## Execution Steps
- [x] Define Business Logic Modeling (Batching and Generation workflows)
- [x] Define Domain Model (Users and Transactions schema)
- [x] Define Business Rules (Mock data constraints, PII generation)
- [x] Define Data Flow (File writing and format specifications)

## Clarification Questions
Before proceeding to generate the functional design artifacts, please answer the following questions to resolve ambiguities in the unit's responsibilities:

**Q1: Business Logic Modeling (Incremental Batches)**
For the incremental batching simulation, how should the historical Apple Stock data (40+ years) be divided? (e.g., Initial bulk load of 30 years, followed by 10 subsequent yearly incremental batches).
`[Answer]:`Initial bulk load of 20 years, followed by 20 subsequent yearly incremental batches

**Q2: Domain Model (User Volume & Cardinality)**
Roughly how many synthetic users should the simulator generate? (e.g., 10,000 users). Since the AAPL data provides the dates and prices, should the simulator just randomly assign these transactions across generated users with random trade volumes?
`[Answer]:` 1,000 users

**Q3: Business Rules (Geography Distribution)**
To explicitly test the `LatamAnalyst` row-level security persona, which Latin American countries and regions should the synthetic users be assigned to? (e.g., random spread, but guarantee at least 30% are from MX, BR, AR, CO).
`[Answer]:`  random spread, but guarantee at least 30% are from MX, BR, AR, CO

**Q4: Data Flow (Raw Format)**
The requirements specify producing CSV/Parquet files for the `raw-zone`. Would you prefer the simulator to write standard CSV files to mock a typical enterprise raw dump, or strictly compressed Parquet files?
`[Answer]:` strictly compressed Parquet files
