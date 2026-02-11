import requests
import os
# from twilio.rest import Client
#
#
# account_sid = os'AC57659d8fa024217d92a522b576b2b961'
# auth_token ='628947f1a75cd83f3919025fa275fc7e'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     body="i love coding!",
#     from_="+18105103860",
#     to="+447803430414"
# )


account_sid=os.environ.get("ACCOUNT_SID")
print(account_sid)

# print(message.body)

LAT = 52.636879
LONG=-1.139759
API_KEY="ce531bf833190f4cd0b79dc82942d7a3"
ENDPOINT="https://api.openweathermap.org/data/2.5/forecast?"

parameters={

    # "q":"London",
    "lat":LAT,
    "lon":LONG,
    "appid":API_KEY,
    "cnt":4

}

response =  requests.get(ENDPOINT,params=parameters)
response.raise_for_status()
weather_data=response.json()

will_rain=False

for i in weather_data["list"]:
    if i["weather"][0]["id"] <=700:
        will_rain=True

if will_rain:
    print("bring an umbrella")


print("test")


