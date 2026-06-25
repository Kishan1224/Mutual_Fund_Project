# Data Dictionary

## Project Overview

This document describes the datasets used in the Mutual Fund Analytics project. It provides a brief explanation of each dataset, the columns available, their data types, and their business significance. The datasets were collected from AMFI, MFAPI, and project-specific sources and were cleaned before loading into the SQLite database.

---

## 1. Fund Master Dataset (01_fund_master.csv)

**Source:** AMFI Fund Master Data

This dataset contains basic information about mutual fund schemes and serves as the primary reference table for all scheme-related analysis.

| Column       | Data Type | Description                                  |
| ------------ | --------- | -------------------------------------------- |
| amfi_code    | Integer   | Unique scheme code assigned by AMFI          |
| scheme_name  | Text      | Name of the mutual fund scheme               |
| fund_house   | Text      | Asset Management Company managing the scheme |
| category     | Text      | Broad fund category                          |
| sub_category | Text      | Detailed fund classification                 |
| plan         | Text      | Direct or Regular plan                       |
| risk_grade   | Text      | Risk level assigned to the scheme            |

---

## 2. NAV History Dataset (02_nav_history.csv)

**Source:** MFAPI Historical NAV Data

This dataset stores historical Net Asset Value (NAV) information for mutual fund schemes.

| Column    | Data Type | Description                    |
| --------- | --------- | ------------------------------ |
| amfi_code | Integer   | Scheme identifier              |
| date      | Date      | Date on which NAV was recorded |
| nav       | Decimal   | Net Asset Value of the scheme  |

---

## 3. AUM by Fund House Dataset (03_aum_by_fund_house.csv)

**Source:** AMFI Industry Statistics

This dataset provides Assets Under Management (AUM) information for different fund houses.

| Column     | Data Type | Description               |
| ---------- | --------- | ------------------------- |
| fund_house | Text      | Name of the AMC           |
| aum_crore  | Decimal   | Total AUM in crore rupees |
| month      | Date      | Reporting month           |

---

## 4. Monthly SIP Inflows Dataset (04_monthly_sip_inflows.csv)

**Source:** AMFI Monthly Reports

This dataset tracks monthly SIP investments made by investors.

| Column           | Data Type | Description                   |
| ---------------- | --------- | ----------------------------- |
| month            | Date      | Reporting month               |
| sip_amount_crore | Decimal   | SIP inflow amount in crores   |
| sip_accounts     | Integer   | Number of active SIP accounts |

---

## 5. Category Inflows Dataset (05_category_inflows.csv)

**Source:** Mutual Fund Industry Data

This dataset contains fund flow information for different mutual fund categories.

| Column       | Data Type | Description                  |
| ------------ | --------- | ---------------------------- |
| category     | Text      | Mutual fund category         |
| month        | Date      | Reporting month              |
| inflow_crore | Decimal   | Net inflow or outflow amount |

---

## 6. Industry Folio Count Dataset (06_industry_folio_count.csv)

**Source:** AMFI Statistics

This dataset shows the number of investor folios maintained across the industry.

| Column      | Data Type | Description                     |
| ----------- | --------- | ------------------------------- |
| month       | Date      | Reporting month                 |
| folio_count | Integer   | Total number of investor folios |

---

## 7. Scheme Performance Dataset (07_scheme_performance.csv)

**Source:** Scheme Performance Records

This dataset contains return and risk-related metrics used for performance evaluation.

| Column             | Data Type | Description                          |
| ------------------ | --------- | ------------------------------------ |
| amfi_code          | Integer   | Unique AMFI scheme code              |
| scheme_name        | Text      | Name of the scheme                   |
| fund_house         | Text      | Managing AMC                         |
| category           | Text      | Fund category                        |
| plan               | Text      | Direct or Regular plan               |
| return_1yr_pct     | Decimal   | One-year return percentage           |
| return_3yr_pct     | Decimal   | Three-year return percentage         |
| return_5yr_pct     | Decimal   | Five-year return percentage          |
| benchmark_3yr_pct  | Decimal   | Benchmark return percentage          |
| alpha              | Decimal   | Excess return over benchmark         |
| beta               | Decimal   | Market sensitivity measure           |
| sharpe_ratio       | Decimal   | Risk-adjusted return metric          |
| sortino_ratio      | Decimal   | Downside risk-adjusted return metric |
| std_dev_ann_pct    | Decimal   | Annualized volatility                |
| max_drawdown_pct   | Decimal   | Maximum decline from peak value      |
| aum_crore          | Decimal   | Assets Under Management              |
| expense_ratio_pct  | Decimal   | Expense ratio charged by the fund    |
| morningstar_rating | Integer   | Morningstar rating score             |
| risk_grade         | Text      | Risk category assigned to the fund   |

---

## 8. Investor Transactions Dataset (08_investor_transactions.csv)

**Source:** Investor Transaction Records

This dataset stores transaction-level information related to investor activities.

| Column           | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| transaction_id   | Integer   | Unique transaction number   |
| amfi_code        | Integer   | Related scheme code         |
| investor_id      | Integer   | Investor identifier         |
| transaction_type | Text      | SIP, Lumpsum, or Redemption |
| amount           | Decimal   | Transaction amount          |
| transaction_date | Date      | Date of transaction         |
| state            | Text      | Investor state              |
| kyc_status       | Text      | KYC verification status     |

---

## 9. Portfolio Holdings Dataset (09_portfolio_holdings.csv)

**Source:** Portfolio Disclosure Data

This dataset contains information about securities held by mutual fund schemes.

| Column       | Data Type | Description                            |
| ------------ | --------- | -------------------------------------- |
| amfi_code    | Integer   | Scheme identifier                      |
| holding_name | Text      | Name of the security                   |
| sector       | Text      | Industry sector                        |
| weight_pct   | Decimal   | Percentage allocation in the portfolio |

---

## 10. Benchmark Indices Dataset (10_benchmark_indices.csv)

**Source:** Market Benchmark Data

This dataset stores benchmark index values used for comparison against fund performance.

| Column      | Data Type | Description                          |
| ----------- | --------- | ------------------------------------ |
| date        | Date      | Trading date                         |
| index_name  | Text      | Benchmark index name                 |
| index_value | Decimal   | Closing value of the benchmark index |

---

## Summary

The above datasets collectively provide information related to mutual fund schemes, NAV history, fund performance, investor activity, SIP trends, AUM statistics, and benchmark performance. These datasets were cleaned, validated, and loaded into a SQLite database to support analytical reporting and dashboard development.
