# Write a query that will calculate the number of shipments per month. The unique key for one shipment is a combination of shipment_id and sub_id.
# Output the year_month in format YYYY-MM and the number of shipments in that month.



#different solutions:

df = amazon_shipment
df['year_month'] = df['shipment_date'].dt.strftime('%Y-%m')
df.groupby('year_month')['shipment_id'].count().reset_index()



df = amazon_shipment
df['year_month'] = pd.to_datetime(df['shipment_date']).dt.to_period('M')
df.groupby('year_month').size().to_frame('num_of_shipment').reset_index()


df = amazon_shipment.copy()
df.groupby(df["shipment_date"].dt.strftime("%Y-%m")).agg({"shipment_id":"count"}).reset_index()