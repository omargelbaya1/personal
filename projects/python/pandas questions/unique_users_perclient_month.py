# Write a query that returns the number of unique users per client for each month. Assume all events occur within the same year, so only month needs to be be in the output as a number from 1 to 12.
# Import your libraries
import pandas as pd

fact_events['month'] = fact_events['time_id'].dt.month

fact_events.groupby(['client_id', 'month'])['user_id'].nunique().reset_index()



#ORRRRR:
import pandas as pd

result = (
    fact_events.groupby(
        [fact_events["client_id"], fact_events["time_id"].dt.month]
    )["user_id"]
    .nunique()
    .reset_index()
)
result = result.rename(columns={"time_id": "month", "user_id": "users_num"})



