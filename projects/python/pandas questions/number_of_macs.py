# --Count the number of user events performed by MacBookPro users.
# Output the result along with the event name.
# Sort the result based on the event count in the descen
# ding order.


#variations of solutions:
# Import your libraries
import pandas as pd

# Start writing code
df = playbook_events
df.loc[df.device == 'macbook pro', 'event_name'].value_counts().reset_index()


macbook_device = playbook_events[playbook_events["device"] == "macbook pro"]
result = (
    macbook_device.groupby(["event_name"])
    .size()
    .to_frame("size")
    .reset_index()
    .sort_values(["size"], ascending=False)
    .rename(columns={"size": "event_count"})


playbook_events.head()
macbook = playbook_events.loc[playbook_events['device'] == 'macbook pro']
result = macbook.groupby(['event_name'])['user_id'].count().to_frame('event_count').reset_index().sort_values('event_count', ascending=False)