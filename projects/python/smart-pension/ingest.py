import requests
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

#Loading in environment variables
load_dotenv()

#Parameters for database connection
host="localhost"
database=os.getenv("DATABASE")
user=os.getenv("DATABASE_USER")
password=os.getenv("DATABASE_PASSWORD")
port=os.getenv("DATABASE_PORT")


#testing database Connection
try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    print("Connection successful!")
    conn.close()
except psycopg2.OperationalError as e:
    print(f"Connection failed: {e}")




#Parameeters for the weather ingestion
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": [51.51, 53.48, 55.95, 51.45],
	"longitude": [-0.13, -2.24, -3.19, -2.58],
	"daily": ["temperature_2m_min", "temperature_2m_max", "precipitation_sum"],
}
cities = [ 'London','Manchester','Edinburgh','Bristol']


#calling API to get weather data
response = requests.get(url,params=params)
data = response.json()





#Inserting the city into the data for each specific long/lat entry
for i, entry in enumerate(data):
    entry["daily"]["city"] = cities[i]


#creating a row per day per city for the above data
combined_data=[]
for entry in data:
    for i, date in enumerate(entry["daily"]['time']):
        combined_data.append({
            'city':             entry["daily"]['city'],
            'date':             date,
            'temp_max_c': entry["daily"]['temperature_2m_max'][i],
            'temp_min_c':         entry["daily"]['temperature_2m_min'][i],
            'precipitation_mm': entry["daily"]['precipitation_sum'][i],
        })

#creating pandas dataframe from above data
df = pd.DataFrame(combined_data)
print(df.to_string)



#inserting df into postgre table
#Unsure if it needs to append to replace here
#Using index=False to stop the dataframe index being inserted as a column
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

try:
    df.to_sql('raw_weather',engine ,if_exists='append',index=False)
    print("Successfully inserted database into database")
except ValueError as e:
    print(f"Database insert failed {e}")








