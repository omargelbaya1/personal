from sys import exception

import requests
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
from requests import HTTPError
from sqlalchemy import create_engine

#Loading in environment variables
load_dotenv()



#Parameters for database connections
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



#Parameters for the weather ingestion
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": [51.51, 53.48, 55.95, 51.45],
	"longitude": [-0.13, -2.24, -3.19, -2.58],
	"daily": ["temperature_2m_min", "temperature_2m_max", "precipitation_sum"],
}

#calling API to get weather data
#checking if response returns a 200 status code for success
try:
    response = requests.get(url,params=params)
    response.raise_for_status()

    if response.status_code ==200:
        print(f"Successful retrieval of data. Response Code: {response.status_code}")
        data = response.json()
except HTTPError as e:
    print(f"Unsuccessful retrieval of data {e}")
    raise exception ("")






#Inserting the city into the data for each specific long/lat entry
cities = [ 'London','Manchester','Edinburgh','Bristol']
for i, entry in enumerate(data):
    entry['daily']["city"] = cities[i]





#Checking if key/values are nulls in response
keys_to_check=['time','temperature_2m_min','temperature_2m_max','precipitation_sum']
for entry in data:
    for key in keys_to_check:
        if key not in entry['daily'] or not entry['daily'][key]:
            print(f"{key} not present in {entry['daily']['city']} data or no values present")


#creating a row per day per city for the above data
combined_data=[]
for entry in data:
    for i, date in enumerate(entry["daily"]['time']):
        combined_data.append({
            'city': entry['daily']['city'],
            'date': date,
            'temp_max_c': entry['daily']['temperature_2m_max'][i],
            'temp_min_c': entry['daily']['temperature_2m_min'][i],
            'precipitation_mm': entry['daily']['precipitation_sum'][i],
        })


#creating pandas dataframe from above data
df = pd.DataFrame(combined_data)
print(df.to_string)



#inserting dataframe into postgre table
#Using index=False to stop the dataframe index being inserted as a column
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

try:
    df.to_sql('raw_weather',engine ,if_exists='replace',index=False)
    print("Successfully inserted data into database")
except ValueError as e:
    print(f"Database insert failed {e}")








