#-----------------------------------------IMPORTS----------------------------------------------------#
from smtplib import SMTP

import time
import requests
import datetime as dt

#--------------------------------------CONSTANTS/VARIABLES-------------------------------------------#
HORSELL_LAT = 51.327919
HORSELL_LONG = -0.569540

MY_EMAIL = "elijclarke0@gmail.com"
MY_PASSWORD = "esji sxjt elcb fwxy"
EMAILS = ["elijaclarke@gmail.com","philippa_hoyle@hotmail.co.uk"]

#---------------------------------------GET ISS POSITION----------------------------------------------#
def compare_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    longitude = float(response.json()['iss_position']['longitude']).__round__()
    latitude = float(response.json()['iss_position']['latitude']).__round__()

    if longitude in range(int(HORSELL_LONG)-5,int(HORSELL_LONG)+5) and latitude in range(int(HORSELL_LAT)-5,int(HORSELL_LAT)+5):
        for email in EMAILS:
            send_email(recipient=email)

#------------------------------------GET SUNSET AND SUNRISE IN HORSELL------------------------------#
def get_sun():
    global cur_time
    now = dt.datetime.now()
    hour = now.time().hour
    minute = now.time().minute
    second = now.time().second
    cur_time = f"{hour}:{minute}:{second}"

    time_check = str(now.hour)
    parameters = {
        "lat": HORSELL_LAT,
        "lng": HORSELL_LONG,
        "formatted": 0
    }

    sunset_response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()

    sunset = sunset_response.json()['results']['sunset'].split('T')[1].split(':')[0]
    sunrise = sunset_response.json()['results']['sunrise'].split('T')[1].split(':')[0]
    if time_check > sunset or time_check < sunrise:
        compare_iss()


#--------------------------------------------SEND EMAIL----------------------------------------------#
def send_email(recipient):
    global cur_time
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=recipient,
                            msg=f"Subject:Look up!\n\nThe International Space Station is currently above Horsell and visible in the night sky!\nThe ISS went over Horsell at {cur_time} today."
        )

#--------------------------------------CHECK TIME EVERY 60 SECONDS-----------------------------------#
def check_sun():
    while True:
        get_sun()
        time.sleep(60)
check_sun()

