# You are given a dataset of health inspections that includes details about violations.
# Each row represents an inspection, and if an inspection resulted in a violation, the violation_id column will contain a value.
# Count the total number of violations that occurred at 'Roxanne Cafe' for each year, based on the inspection date.
# Output the year and the corresponding number of violations in ascending order of the year.


# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()


df=sf_restaurant_health_violations

df=df[df['business_name'] == 'Roxanne Cafe']
df.groupby((df["inspection_date"]).dt.year)["violation_id"].count().reset_index()



#another example:
import pandas as pd
import datetime as dt

df = sf_restaurant_health_violations
result = (
    df[(df['business_name'] == 'Roxanne Cafe') & (~df['violation_id'].isna())]
    .groupby(pd.to_datetime(df['inspection_date']).dt.year)['violation_id']
    .count()
    .reset_index()
    .rename(columns={'inspection_date': 'inspection_year', 'violation_id': 'n_violations'})
)
