#----------------------------------------------------IMPORTS-----------------------------------------------------------#
import json
from smtplib import *
import datetime as dt
#------------------------------------------------CONSTANTS/VARIABLES---------------------------------------------------#

MY_EMAIL = "elijclarke0@gmail.com"
MY_PASSWORD = "esji sxjt elcb fwxy"
now = dt.datetime.now()
day = now.day
month = now.month
date = f"{day}|{month}"

#----------------------------------------------------SEND EMAIL--------------------------------------------------------#

def send_email(name,email):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy birthday {name}\n\nHi {name}\n\n Have an amazing birthday!\n\nSent with love,\nEli"
        )

#----------------------------------------------------CHECK_DAY---------------------------------------------------------#

def check_date():
    with open("friends.json") as file:
        friends = json.load(file)
        for friend,details in friends.items():
            if list(details.values())[0] == date:
                chosen_friend = friend
                chosen_email = list(details.keys())[0]
                send_email(name=chosen_friend,email=chosen_email)
check_date()








