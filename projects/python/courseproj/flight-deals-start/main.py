#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

new_flight= FlightSearch()
new_data=DataManager()

# new_flight.get_access_token()

cities_list=new_data.get_data()


iata_list=new_flight.get_iata_code(cities_list)


new_data.update_iata_code(iata_list)

new_flight.get_cheapest_flight()



# new_flight.get_access_token()

