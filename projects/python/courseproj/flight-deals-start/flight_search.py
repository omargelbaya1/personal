import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_KEY=""
        self.API_SECRET=""
        self.endpoint="https://test.api.amadeus.com/v1/security/oauth2/token"
        self.headers_token={ "Content-Type": "application/x-www-form-urlencoded"}
        self.parameters_token={
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }
        self.ACCESS_TOKEN=""

        self.iata_code_list=[]
        self.iata_get_url="https://test.api.amadeus.com/v1/reference-data/locations"
        self.iata_parameters={
            "subType":"CITY",
            "keyword":"Paris"
        }
        self.iata_header={
           "Authorization": f"Bearer {self.ACCESS_TOKEN}",
           "Accept": "application/json",
        }

        self.flight_url="https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.flight_parameters={"originLocationCode": "LON",      # e.g., LHR, LGW, or city code LON
        "destinationLocationCode": "NYC", # e.g., JFK/EWR or city code NYC
        "departureDate": "2026-03-10",    # YYYY-MM-DD
          }                    # optional: number of offers

    # def get_access_token(self):
    #     response=requests.post(self.endpoint,headers=self.headers_token,data=self.parameters_token)
    #     response.raise_for_status()
    #     data=response.json()
    #     access_token=data["access_token"]
    #     print(access_token)
    #     return access_token

    def get_iata_code(self,city_list):
        for i in city_list:
            self.iata_parameters["keyword"]=i
            response=requests.get(self.iata_get_url,params=self.iata_parameters,headers=self.iata_header)
            response.raise_for_status()
            data=response.json()
            iata_code=data["data"][0]["address"]["cityCode"]
            self.iata_code_list.append(iata_code)
        return self.iata_code_list


    def get_cheapest_flight(self):
        response=requests.get(self.flight_url,headers=self.iata_header,params=self.flight_parameters)
        response.raise_for_status()
        print(response.json())
        print(response.text)


