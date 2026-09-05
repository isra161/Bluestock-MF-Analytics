# Data Dictionary

This file explains the main columns used in the Bluestock Mutual Fund Analytics project.

## 1. Fund Master

| Column | Meaning |
|---|---|
| amfi_code | Unique code given to a mutual fund scheme |
| fund_house | Name of the company managing the fund |
| category | Main category of the fund |
| sub_category | More specific type of the fund |
| risk_category | Risk level of the fund |

## 2. NAV History

| Column | Meaning |
|---|---|
| amfi_code | Code of the mutual fund scheme |
| date | Date on which NAV was recorded |
| nav | Net Asset Value of the fund |

## 3. Investor Transactions

| Column | Meaning |
|---|---|
| investor_id | Unique ID of the investor |
| transaction_date | Date of the transaction |
| amfi_code | Mutual fund scheme code |
| transaction_type | Type of transaction such as SIP, Lumpsum or Redemption |
| amount_inr | Amount invested or redeemed in INR |
| state | State of the investor |
| city | City of the investor |
| city_tier | Classification of the city |
| age_group | Age group of the investor |
| gender | Gender of the investor |
| annual_income_lakh | Annual income of the investor in lakh |
| payment_mode | Method used to make the payment |
| kyc_status | Current KYC verification status |

## 4. Scheme Performance

| Column | Meaning |
|---|---|
| amfi_code | Mutual fund scheme code |
| scheme_name | Name of the scheme |
| fund_house | Company managing the fund |
| category | Category of the mutual fund |
| plan | Type of investment plan |
| return_1yr_pct | Return generated over 1 year |
| return_3yr_pct | Return generated over 3 years |
| return_5yr_pct | Return generated over 5 years |
| benchmark_3yr_pct | Benchmark return for 3 years |
| alpha | Performance of the fund compared with its benchmark |
| beta | Indicates how the fund moves compared with the market |
| sharpe_ratio | Measures return considering the risk taken |
| sortino_ratio | Measures return considering downside risk |
| std_dev_ann_pct | Annualized variation in fund returns |
| max_drawdown_pct | Largest fall in fund value |
| aum_crore | Assets under management in crore |
| expense_ratio_pct | Percentage charged as fund expenses |
| morningstar_rating | Rating given to the fund |
| risk_grade | Risk grade of the fund |
| expense_ratio_anomaly | Shows whether the expense ratio needs attention |

## Data Cleaning Rules

- Duplicate records were removed.
- NAV values were checked to make sure they are greater than 0.
- Transaction types were standardized as SIP, Lumpsum and Redemption.
- Transaction amounts were checked for positive values.
- Dates were converted into a standard date format.
- Return-related columns were converted to numeric values.
- Expense ratio was checked against the 0.1% to 2.5% range.
- Records outside the expected expense ratio range were flagged.