import pandas as pd

transactions = pd.read_csv(
    r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\data\raw\08_investor_transactions.csv"
)

# Standardize transaction type
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Allow only valid transaction types
valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

transactions = transactions[
    transactions["transaction_type"].isin(valid_types)
]

# Convert transaction date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Keep positive amounts only
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Valid KYC values
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

transactions = transactions[
    transactions["kyc_status"].isin(valid_kyc)
]

# Save cleaned file
transactions.to_csv(
    r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\data\processed\08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor transactions cleaned successfully.")