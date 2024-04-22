#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
from data_manager import DataManager

sheet_data = DataManager().get_response()
print(sheet_data)
for entry in sheet_data:
    entry['iataCode'] = 'TESTING'
print(sheet_data)

