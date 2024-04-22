#-------------------------------IMPORTS------------------------#
import sys

import requests
import datetime as dt

#------------------------------CONSTANTS----------------------#
USERNAME = 'eliclarkecode'
TOKEN = ')2c&*KPq8pz2+C2C'

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_PARAMS ={
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

now = (dt.datetime.now()).strftime('%Y%m%d')

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_id = "graph1"
graph_name = "coding_graph"
graph_params = {
    'id': graph_id,
    'name': graph_name,
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}
graph_headers = {
    'X-USER-TOKEN': TOKEN
}

#--------------------------------POST PIXEL---------------------------#
def post_pixel():
    quantity = input("How many minutes did you spend coding today?")
    add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"
    add_pixel_params = {
        'date': now,
        'quantity': quantity,

    }
    response = requests.post(url=add_pixel_endpoint,json=add_pixel_params, headers=graph_headers)
    print(response.text)

#--------------------------------UPDATE PIXEL-------------------------#
def update_pixel():
    quantity = input("How many minutes did you spend coding today?")
    update_pixel_endpoint = f"{graph_endpoint}/{graph_id}/{now}"
    update_pixel_params = {
        'quantity': quantity,
    }
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=graph_headers)
    print(response.text)

#-------------------------------DELETE PIXEL--------------------------#
def delete_pixel():
    update_pixel_endpoint = f"{graph_endpoint}/{graph_id}/{now}"
    response = requests.delete(url=update_pixel_endpoint, headers=graph_headers)
    print(response.text)

#--------------------------------MENU----------------------------------#
def menu():
    choice = input(
        "What would you like to do?\n"
        "Create new pixel [1]\n"
        "Update today's pixel [2]\n"
        "Delete today's pixel [3]\n"
        "Exit program [4]\n"
    )
    if choice == "1":
        post_pixel()
    elif choice == "2":
        update_pixel()
    elif choice == "3":
        delete_pixel()
    elif choice == "4":
        sys.exit()
    menu()
menu()