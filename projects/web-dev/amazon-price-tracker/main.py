import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()


header={"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-69a845d2-0874e2fc032838742bf1dd05"

}




url = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Stainless/dp/B00OP26T4K/ref=sr_1_1_sspa?crid=OID5XLXOCKGM&dib=eyJ2IjoiMSJ9.luyDQsWGnxgY1FNKzfH3A4pmpkBbKVnsDK0fHzqqytEXZzOQ8MVJ3nvYde3KUbQbVsHUBQPmE-ebyfBuvwE8_abmS8SF75gSOoEuY-tptz9wrsrsHg9DZrLqdtOvUZ-XZd_W6Qm_hMjJHMj9dsig_7NyOffdz3MLKviPPkCS9O5--Xi4Z66U824yihG6dfESX9WWxGh3Yzb0QiRPRE5Mx67MPE1C1tR50YXA1J1qzMM.ADKBHsUsFSq5QKksnFg2LKeMxSo-bpOYQEZYxMXwskM&dib_tag=se&keywords=instant%2Bpot%2Bduo&qid=1772635779&sprefix=instant%2Bpot%2Bduo%2Caps%2C297&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.95fd378e-6299-4723-b1f1-3952ffba15af&aref=InODXPI2eh&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')


price = soup.find(class_="a-offscreen").get_text()
print(price)
price_without_currency = price.split("£")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

name_of_product=soup.find(class_="a-size-large product-title-word-break").get_text()



http_api=os.getenv("HTTP_API")
bot_username=os.getenv("BOT_USERNAME")
chat_id=os.getenv("CHAT_ID")
message=f"the current price of has gone below £100 and is now £{price_as_float}"

if price_as_float <= 100:
    url_telegram=f"https://api.telegram.org/bot{http_api}/sendMessage?chat_id={chat_id}&text={message}"
    url_telegram_2=f"https://api.telegram.org/bot{http_api}/sendMessage?chat_id={chat_id}&text={name_of_product}"

    r=requests.get(url_telegram)
    y2 = requests.get(url_telegram_2)
