import pandas as pd

performance = pd.read_csv(
    "C:\\Users\\puvvu\\OneDrive\\ドキュメント\\MutualFundProject\\data\\processed\\07_scheme_performance_cleaned.csv"
)

risk = input(
    "Enter Risk (Low/Moderate/High): "
)

result = performance[
    performance["risk_grade"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

result = result.sort_values(
    "sharpe_ratio",
    ascending=False
)

print(
    result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)
)