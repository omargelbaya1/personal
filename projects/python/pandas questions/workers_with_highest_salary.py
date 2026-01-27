# Management wants to analyze only employees with official job titles. Find the job titles of the employees with the highest salary. If multiple employees have the same highest salary, include all their job titles.

df =pd.merge(worker,title,left_on='worker_id',right_on='worker_ref_id')
df[df['salary']== df['salary'].max()][['worker_title']]



#other solution:

# Import your libraries
import pandas as pd

# Start writing code
worker.head()

worker[worker.salary == worker.salary.max()].merge(title, how = 'inner', left_on = 'worker_id', right_on = 'worker_ref_id')[['worker_title']]




# Import your libraries
import pandas as pd

# Start writing code
output = worker[worker['salary'] == worker['salary'].max()]
data = pd.merge(output, title, left_on = 'worker_id', right_on='worker_ref_id', how='inner')