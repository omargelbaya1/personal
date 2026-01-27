# Find the number of employees working in the Admin department that joined in April or later, in any year.

#examples of solutions:

admin = worker[(worker['department'] == 'Admin') & (worker['joining_date'].dt.month >= 4)]
r1 = admin['worker_id'].count()