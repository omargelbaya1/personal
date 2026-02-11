import requests
import datetime as dt
from itertools import islice

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK='263JZ1OIUUUSBQUL'
NEWS_API_KEY='344307b03ff4471e8838c56999e64dc1'


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

yesterday=(dt.datetime.now() - dt.timedelta(1)).date()
day_before_yesterday=(dt.datetime.now() - dt.timedelta(2)).date()
print(yesterday,day_before_yesterday)


# def get_stock_value(date):
#
#     parameters_stock={
#         "function":"HISTORICAL_OPTIONS",
#         "symbol":STOCK,
#         "date":date,
#         "apikey":API_KEY_STOCK
#     }
#
#     response_stock = requests.get(
#         "https://www.alphavantage.co/query", params=parameters_stock
#     )
#     response_stock.raise_for_status()
#     stock_data=response_stock.json()
#     closing_value=0
#     for i in stock_data["data"]:
#         closing_value=(i["strike"])
#     return closing_value
#
#
#
#
# def compare_prices(value1,value2):
#     print("work")
#     diff=abs(value2-value1)
#     if (diff/value1)*100 >=5:
#         print("got news")
#         percentage=((diff/value1)*100)
#         print(f"{percentage}%")
#
# yesterday_value=get_stock_value(yesterday)
# day_before_yesterday_value=get_stock_value(day_before_yesterday)
#
# compare_prices(yesterday_value,day_before_yesterday_value)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news(date):
    parameters_news = {
        "q": STOCK,
        "from": date,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,

    }

    response_news = requests.get("https://newsapi.org/v2/everything?", params=parameters_news)
    response_news.raise_for_status()
    news_data = response_news.json()
    print(news_data)
    news_list=list(news_data.items())[:3]
    print(news_list)

get_news(yesterday)
## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


parameters_sms={
    "placeholder":STOCK,
    "placeholder_api_key":API_KEY_STOCK
}


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




