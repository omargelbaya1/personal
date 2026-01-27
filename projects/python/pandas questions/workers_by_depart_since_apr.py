# Find the number of workers by department who joined on or after April 1, 2014.
#
#
# Output the department name along with the corresponding number of workers.
#
#
# Sort the results based on the number of workers in descending order.


worker['joining_date'] = pd.to_datetime(worker['joining_date'])

filtered = worker[worker['joining_date'] >= pd.to_datetime('2014-04-01')]
result = (
    filtered.groupby('department')
    .size()
    .reset_index(name='num_workers')
    .sort_values(by='num_workers', ascending=False)
)



# Import your libraries
import pandas as pd

# Start writing code
worker.head()
worker[worker['joining_date'].dt.month >= 4].groupby(['department']).size().reset_index(name = 'num_workers').sort_values(by = 'num_workers', ascending = False)