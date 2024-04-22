#----------------------------------------------------IMPORTS-----------------------------------------------------------#
from smtplib import *
import datetime as dt
import random
#------------------------------------------------CONSTANTS/VARIABLES---------------------------------------------------#

MY_EMAIL = "elijclarke0@gmail.com"
MY_PASSWORD = "esji sxjt elcb fwxy"
EMAILS = ["elijaclarke@gmail.com","philippa_hoyle@hotmail.co.uk"]
now = dt.datetime.now()
day_of_week = now.weekday()
FRIDAY = 4

#--------------------------------------------------GENERATE QUOTE------------------------------------------------------#

def generate_quote():
    global chosen_quote
    with open("quotes.txt") as file:
        quotes = file.readlines()
        chosen_quote = random.choice(quotes)

#----------------------------------------------------SEND EMAIL--------------------------------------------------------#

def send_email(recipient,quote):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient, msg=f"Subject:Happy Friday!\n\n{quote}")

#----------------------------------------------------CHECK_DAY---------------------------------------------------------#

if day_of_week == FRIDAY:
    for email in EMAILS:
        generate_quote()
        send_email(recipient=email,quote=chosen_quote)







