import pandas as pd






def problem():
    df = pd.read_csv("/Users/omargelbaya/Documents/personal/projects/python/hasting_direct/prob-one/data.csv")
    df.columns = df.columns.str.strip()
    df['risk_score'] = df['risk_score'].replace(' ', 1.10).astype(float)
    # 1. Where risk_score is missing → 1.10 uplift on premium
    mask_missing = df['risk_score'].isna()
    # 2. Where risk_score > 0.7 → 1.15 uplift on premium
    mask_high = df['risk_score'] > 0.7
    # 3. Apply them separately to base_premium
    df.loc[mask_missing, 'base_premium'] *= 1.10
    df.loc[mask_high, 'base_premium'] *= 1.15
    df['risk_score'] = df['risk_score'].astype(float)
    df['base_premium'] = df['base_premium'].astype(float)
    avg = df.groupby('region').mean(numeric_only=True)["base_premium"]
    # highest_value=df[' risk_score'].max()[" base_premium"]
    highest_value = df.loc[df["risk_score"].idxmax(), ["base_premium", "risk_score"]]
    return print(avg, highest_value)

problem()





