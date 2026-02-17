#BELOW IS A WORKING METHOD TO SEND SMS, you can automate the stocks stuff from below:
import requests
http_api="8335945594:AAG2lzi7U4Lplql4PazKQF028Ati92I-40w"
bot_username="@testomarge"
# url=f"https://api.telegram.org/bot{http_api}/getUpdates"
chat_id="7775372810"
#
# response=requests.get(url)
# response.raise_for_status()
# print(response.text)
# print(response.json())
message="wag1 g"
url=f"https://api.telegram.org/bot{http_api}/sendMessage?chat_id={chat_id}&text={message}"
r=requests.get(url)
print(r.json())
