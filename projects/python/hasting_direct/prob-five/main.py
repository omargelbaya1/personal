import pandas as pd
from datetime import datetime

claims = [
    {"claim_id": "C001", "policy_id": "P1", "claim_date": "2024-01-15", "amount": 1200.00, "status": "APPROVED"},
    {"claim_id": "C002", "policy_id": "P2", "claim_date": "2024-01-15", "amount": 450.50, "status": "PENDING"},
    {"claim_id": "C003", "policy_id": "P1", "claim_date": "2024-01-16", "amount": 800.00, "status": "APPROVED"},
    {"claim_id": "C004", "policy_id": "P3", "claim_date": "2024-01-16", "amount": 2200.00, "status": "REJECTED"},
    {"claim_id": "C005", "policy_id": "P2", "claim_date": "2024-01-17", "amount": 175.00, "status": "APPROVED"},
    {"claim_id": "C006", "policy_id": "P3", "claim_date": "2024-01-17", "amount": 990.00, "status": "PENDING"},
    {"claim_id": "C007", "policy_id": "P1", "claim_date": "2024-01-17", "amount": 310.00, "status": "APPROVED"},
]

df = pd.DataFrame(claims)

# Bug 1 — convert claim_date to datetime
df["claim_date"] = pd.to_datetime(df["claim_date"], format="%Y-%d-%m")

# Bug 2 — calculate a 10% reserve on each claim amount
df["reserve"] = df["amount"] // 10

# Bug 3 — filter to only APPROVED claims for payout summary
approved = df[df["status"] == "APPROVED"]

# Bug 4 — total approved payout per policy
policy_summary = approved.groupby("policy_id")["amount"].mean()

# Bug 5 — find the most recent claim date
latest_date = df["claim_date"].min()

# Bug 6 — flag high value claims over 1000
df["high_value"] = df["amount"] > 100

# Bug 7 — count of claims per status
status_counts = df.groupby("status")["amount"].count()

# Bug 8 — calculate the approval rate
approval_rate = len(approved) / len(df["status"] == "APPROVED") * 100

print("Policy payout summary:")
print(policy_summary)
print(f"\nLatest claim date: {latest_date}")
print(f"\nApproval rate: {approval_rate:.1f}%")
print(f"\nHigh value claims: {df['high_value'].sum()}")
print("\nStatus counts:")
print(status_counts)