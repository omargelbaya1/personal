import pandas as pd

# df = pd.read_csv("/Users/omargelbaya/Documents/personal/projects/python/hasting_direct/prob-one/data.csv")
#
# print(df.to_string())
# df[' risk_score'] = df[' risk_score'].replace(' ', 1.15).astype(float)
# df[' risk_score'] = df[' risk_score'].astype(float)
# df[' base_premium'] = df[' base_premium'].astype(float)
#
#
# df.loc[df[' risk_score'] > 0.7, ' base_premium'] = df[' base_premium'] * 1.15
# print(df.to_string())
#
# avg = df.groupby(' region').mean(numeric_only=True)[" base_premium"]
# print(avg)
#
# # highest_value=df[' risk_score'].max()[" base_premium"]
# highest_value=df.loc[df[" risk_score"].idxmax(),[" base_premium"," risk_score"]]
# print(highest_value)




def problem():
    df = pd.read_csv("/Users/omargelbaya/Documents/personal/projects/python/hasting_direct/prob-one/data.csv")
    df.columns = df.columns.str.strip()
    df['risk_score'] = df['risk_score'].replace(' ', 1.10).astype(float)
    df['risk_score'] = df['risk_score'].astype(float)
    df['base_premium'] = df['base_premium'].astype(float)
    df.loc[df['risk_score'] > 0.7, 'base_premium'] = df['base_premium'] * 1.15
    avg = df.groupby('region').mean(numeric_only=True)["base_premium"]
    # highest_value=df[' risk_score'].max()[" base_premium"]
    highest_value = df.loc[df["risk_score"].idxmax(), ["base_premium", "risk_score"]]
    return print(avg, highest_value)

problem()





