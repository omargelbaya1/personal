# Calculates the difference between the highest salaries in the marketing and engineering departments. Output just the absolute difference in salaries.
# Import your libraries
# well proud of below!!

import pandas as pd

# Start writing code
db_employee

df=db_employee

db=db_dept
merged= df.merge(db,how="inner",right_on='id',left_on='department_id')


engi=merged[merged["department"]=='engineering']
engi_salary=engi['salary'].max()
marketing=merged[merged["department"]=='marketing']
marketing_salary=marketing['salary'].max()

result=abs(marketing_salary-engi_salary)


