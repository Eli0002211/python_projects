# import csv
# temperatures = []
# new_temperatures = []
# with open("weather_data.csv","r") as file:
#     data = csv.reader(file)
#     for row in data:
#         temperature = row[1]
#         temperatures.append(temperature)
#     for temp in temperatures[1::]:
#         temp = int(temp)
#         new_temperatures.append(temp)
#     print(new_temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = data["temp"].mean()
# print(average.round(2))
# max_temp = data["temp"].max()
# print(max_temp)

#Use °F = (°C x 1.8) + 32

# monday = (data[data.day == "Monday"])
#
# print(((int(monday.temp)*1.8)+32))

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colours = data["Primary Fur Color"]


fur_colours_dict = {
    "fur colour": ["grey","cinnamon","black"],
    "count": [0,0,0]
}
for color in fur_colours:
    if color == "Gray":
        fur_colours_dict["count"][0] += 1
    elif color == "Cinnamon":
        fur_colours_dict["count"][1] += 1
    elif color == "Black":
        fur_colours_dict["count"][2] += 1

data = pandas.DataFrame(fur_colours_dict)

fur_data =data[0::]

fur_data.to_csv("fur_colours.csv")