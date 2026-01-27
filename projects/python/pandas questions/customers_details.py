# Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details.
# Sort records based on the customer's first name and the order details in ascending order.


#Use .merge instead of .join, easier to use!
# Import your libraries
import pandas as pd

# Start writing code
customers


df=customers
df1= orders

df.merge(df1,how="left", left_on="id", right_on="cust_id")
[["first_name","last_name","city","order_details"]].sort_values(by=["first_name", "order_details"],ascending=True)



#other solutions, i think its probably better to iteratively do stuff in pandas,makes more sense
# Import your libraries
import pandas as pd

# Start writing code
merged = pd.merge(customers, orders, left_on = 'id', right_on = 'cust_id', how = 'left')

merged[['first_name', 'last_name', 'city', 'order_details']].sort_values(['first_name', 'order_details'])