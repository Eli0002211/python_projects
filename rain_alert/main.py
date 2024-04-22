#------------------------------IMPORTS---------------------------------------#
from smtplib import SMTP

import requests

#-----------------------------CONSTANTS-----------------------------------#

LAT = 51.276562
LON = -0.842150

MY_EMAIL = "elijclarke0@gmail.com"
MY_PASSWORD = "esji sxjt elcb fwxy"
EMAILS = ["elijaclarke@gmail.com","kathyclarke@me.com"]

WEATHER_API_KEY = "1b11ff032a35f60c9b4b81a27d33d4ad"

#-----------------------------GET FORECAST-----------------------------------#
def check_forecast():
    response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}")
    response.raise_for_status()
    forecast_counter = 0
    for num in range(0,4):
        weather = response.json()['list'][num]['weather'][0]['description']
        if weather.split()[1] == "rain":
            forecast_counter += 1
    if forecast_counter > 0:
        for recipient in EMAILS:
            send_email(recipient=recipient)


#-----------------------------SEND EMAIL--------------------------------------#
def send_email(recipient):
    global cur_time
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=recipient,
                            msg="Subject:It's going to rain today!\n\nBring an umbrella!"
        )

#---------------------------CALL FUNCTION-----------------------------------------------#
check_forecast()