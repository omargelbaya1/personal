import requests
import pandas as pd


url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": [51.51, 53.48, 55.95, 51.45],
	"longitude": [-0.13, -2.24, -3.19, -2.58],
	"daily": ["temperature_2m_min", "temperature_2m_max", "precipitation_sum"],
}






response = requests.get(url,params=params)

data = response.json()

# for i in data:
#     print(i["daily"])



# df = pd.json_normalize(
#     data
# )
#
# print(df)

