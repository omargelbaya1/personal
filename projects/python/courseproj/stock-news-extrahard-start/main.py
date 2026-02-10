import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK="3XOZY1YOQ4FNYJPG"



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters_stock={
    "placeholder":STOCK,
    "placeholder_api_key":API_KEY_STOCK
}

response_stock=requests.get("")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

parameters_news={
    "placeholder":STOCK,
    "placeholder_api_key":API_KEY_STOCK
}

response_news=requests.get("")
## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


parameters_sms={
    "placeholder":STOCK,
    "placeholder_api_key":API_KEY_STOCK
}
response_sms=requests.get("")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

