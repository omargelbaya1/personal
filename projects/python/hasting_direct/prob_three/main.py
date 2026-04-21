import pandas as pd

renewals = [
    {"policy_id": "P001", "customer_id": "C1", "old_premium": 400.00, "new_premium": 460.00, "region": "North"},
    {"policy_id": "P002", "customer_id": "C2", "old_premium": 300.00, "new_premium": 290.00, "region": "South"},
    {"policy_id": "P003", "customer_id": "C1", "old_premium": 550.00, "new_premium": 700.00, "region": "North"},
    {"policy_id": "P004", "customer_id": "C3", "old_premium": 200.00, "new_premium": 310.00, "region": "Midlands"},
    {"policy_id": "P005", "customer_id": "C2", "old_premium": 480.00, "new_premium": 481.00, "region": "South"},
    {"policy_id": "P006", "customer_id": "C4", "old_premium": 900.00, "new_premium": 630.00, "region": "North"},
    {"policy_id": "P007", "customer_id": "C3", "old_premium": 150.00, "new_premium": 225.00, "region": "Midlands"},
]

df = pd.DataFrame(renewals,index=None)
print(df.to_string())


df["percentage_change"]=round(((df["new_premium"]-df["old_premium"])/df["old_premium"]) * 100,2)
print(df)
df["percentage_increase"]="NORMAL"
df.loc[df['percentage_change'] >20.0, 'percentage_increase'] = "HIGH_INCREASE"
df.loc[df['percentage_change'] <-20.0, 'percentage_increase'] = "HIGH_DECREASE"

print(df.to_string())

df2=df[df.duplicated(subset="customer_id",keep=False)]
print(df.to_string())
df2=df2.groupby('customer_id')["new_premium"].sum()
print(df.to_string())
print(df2.to_string())

# df=df.groupby("region")["percentage_increase"].count()


df=df[(df['percentage_increase'] == "HIGH_INCREASE") | (df['percentage_increase'] == "HIGH_DECREASE") ]['region'].value_counts()
print(df.to_string())





