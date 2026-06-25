import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# Read datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Load tables
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

# Verify row counts
tables = {
    "dim_fund": fund_master,
    "fact_nav": nav_history,
    "fact_transactions": transactions,
    "fact_performance": performance,
    "fact_aum": aum
}

print("\nRow Count Verification")
print("-" * 40)

for table_name, df in tables.items():
    print(
        f"{table_name}: {len(df)} rows loaded"
    )

print("\nSQLite database created successfully.")