import requests
import datetime as dt
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header={
            "Authorization": "Basic "
        }
        self.endpoint="https://api.sheety.co/f878894ca96eedd8055b5a328db0a5d3/flightDeals/prices"
        self.endpoint_edit="https://api.sheety.co/f878894ca96eedd8055b5a328db0a5d3/flightDeals/prices/"
        self.cities_list=[]
        self.edit_params={
            "price": {
                "iataCode":"x"
            }
        }

    def get_data(self):
        response = requests.get(url=self.endpoint,headers=self.header)
        response.raise_for_status()
        data = response.json()
        for i in data["prices"]:
            self.cities_list.append(i["city"])
        return self.cities_list

    def update_iata_code(self,iata_list):
        for i in iata_list:
            self.edit_params["price"]["iataCode"]=i
            response=requests.put(f"{self.endpoint_edit}{iata_list.index(i)+2}",headers=self.header,json=self.edit_params)
            response.raise_for_status()

