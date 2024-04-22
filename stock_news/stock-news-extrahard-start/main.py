#---------------------------------------------IMPORTS--------------------------------------------------#
from smtplib import SMTP
import requests
from html import unescape
#--------------------------------------------CONSTANTS--------------------------------------------------#
MY_EMAIL = "elijclarke0@gmail.com"
MY_PASSWORD = "esjisxjtelcbfwxy"
RECIPIENT = 'elijaclarke@gmail.com'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "7QZ4J9TN1RTEKPFC"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_PARAMS ={
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'interval': '1min',
    'apikey': STOCK_API_KEY
}
NEWS_API_KEY = '0e138eb009d64115a102ec3528720740'
NEWS_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
NEWS_PARAMS ={
    'apiKey': NEWS_API_KEY,
    'q': 'Tesla',
    'category': 'business',
    'country': 'us',
    'pageSize': 100

}

#-------------------------------------------------CHECK STOCK--------------------------------------------#
def check_stock():
    request = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
    data = request.json()['Time Series (Daily)']
    yesterday = list(data)[0]
    day_before = list(data)[1]

    yesterday_close = float(data[yesterday]["4. close"])
    day_before_close = float(data[day_before]["4. close"])
    stock_change = ((yesterday_close - day_before_close) / day_before_close) * 100
    if stock_change >= 5:
        get_news(increase_decrease='increase', percent=stock_change)
    elif stock_change <= -5:
        get_news(increase_decrease='decrease', percent=stock_change)


#---------------------------------------------------GET NEWS-------------------------------------------#
def get_news(increase_decrease, percent):
    if increase_decrease == 'increase':
        symbol = f'⬆{round(percent)}%'
    else:
        symbol = f'⬇{round(percent)}%'
    request = requests.get(NEWS_ENDPOINT,params=NEWS_PARAMS)
    data = request.json()['articles']
    max_index = 3
    for i in range(min(max_index, len(data))):
        title = (data[i]['title'])
        content = (data[i]['content'])
        source = (data[i]['url'])
        send_email(title=title, content=content, source=source, symbol=symbol)


#--------------------------------------------------SEND EMAIL------------------------------------------#
def send_email(title, content, source, symbol):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        msg = unescape(f'Subject:{STOCK}: {symbol} : {title}\n\n{content}\nRead the full story here: {source}')
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIPIENT,
                            msg=msg.encode('utf-8')
                            )

#-------------------------------------------------FUNCTION CALL----------------------------------------#
check_stock()