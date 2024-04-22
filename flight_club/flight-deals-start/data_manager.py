import requests


class DataManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/ed964f362fdd7611388573fd539d014d/eliFlightDeals/prices"
        self.sheety_token = "X0Gwzh!YV9j6)1!("
        self.sheety_headers = {
            'Authorization': f'Bearer {self.sheety_token}'
        }

    def get_response(self):
        self.response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        self.data = self.response.json()['prices']
        for entry in self.data:
            entry['iataCode'] = 'TESTING'
            requests.put(url=f"{self.sheety_endpoint}/{self.data.index(entry)+1}",headers=self.sheety_headers)
DataManager().get_response()

