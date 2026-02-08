import requests
import datetime as dt

# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data=response.json()["iss_position"]
# print(data)


parameters={
    "lng":2,
    "lat":2,
    "formatted":0
}
response=requests.get( "https://api.sunrise-sunset.org/json",params=parameters)
data=response.json()

sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

current_time_hour= dt.datetime.now().hour

print(sunrise,sunset,current_time_hour)