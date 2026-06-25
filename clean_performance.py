import pandas as pd

# Load the dataset
performance = pd.read_csv(
    r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\data\raw\07_scheme_performance.csv"
)

# Columns containing return values
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert return columns to numeric
for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Convert expense ratio to numeric
performance["expense_ratio_pct"] = pd.to_numeric(
    performance["expense_ratio_pct"],
    errors="coerce"
)

# Flag rows having missing or invalid return values
anomalies = performance[
    performance[return_columns].isnull().any(axis=1)
]

# Save anomalies separately
anomalies.to_csv(
    r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\reports\performance_anomalies.csv",
    index=False
)

# Keep only rows with valid expense ratios
performance = performance[
    (performance["expense_ratio_pct"] >= 0.1)
    &
    (performance["expense_ratio_pct"] <= 2.5)
]

# Remove rows having null values in return columns
performance = performance.dropna(
    subset=return_columns
)

performance.to_csv(
    r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\data\processed\07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme performance dataset cleaned successfully.")
print("Number of anomalies found:", len(anomalies))