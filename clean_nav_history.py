import pandas as pd

nav_df = pd.read_csv(r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\data\raw\02_nav_history.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

nav_df["nav"] = nav_df.groupby(
    "amfi_code"
)["nav"].ffill()

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df["nav"] > 0]

nav_df.to_csv(
   r"C:\Users\puvvu\OneDrive\ドキュメント\MutualFundProject\data\processed\02_nav_history_cleaned.csv",
    index=False
)

print("NAV history cleaned successfully.")