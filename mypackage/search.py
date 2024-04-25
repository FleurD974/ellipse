#cle api : e0a1bf2c844edb9084efc764c089dd748676cc14
import requests
import numpy as np

#communication with the API to get the datas
def get_data(city: str):
  KEY_API = 'e0a1bf2c844edb9084efc764c089dd748676cc14'
  url = 'https://api.jcdecaux.com/vls/v1/stations?contract=' + city + '&apiKey=' + KEY_API
  response = requests.get(url)
  data = response.json()
  return(data)

#a function to extract the number of each station of ONE city (to have more informaiton on station)
def extraction_station_number(data: list):
  number_station = []
  for i in range(len(data)):
    number_station.append(data[i]["number"])
  return(number_station)
  
#function to have the number of bike per city
def extraction_total_bike(data: list):
  number_bike = []
  for i in range(len(data)):
    number_bike.append(data[i]["bike_stands"])
  number_bike2 = np.array(number_bike)
  total_bike = number_bike2.sum()
  return(total_bike)

#function to have the number of station per city
def extraction_number_of_station(data: list):
  number_station = len(data)
  return(number_station)

#fonction to have the total number of bike and station for every supported city in France 
def city_infos(cities):
  stations = []
  number_bike = []
  for city in cities:
    data = get_data(city)
    station_number = extraction_number_of_station(data)
    total_bike = extraction_total_bike(data)
    stations.append(station_number)
    number_bike.append(total_bike)
  return(stations, number_bike)

#fonction to have the position of each station of a contract (to use on the map)
def extraction_position(data:list):
  positions= []
  for i in range(len(data)):
    positions.append(data[i]["position"])
  return(positions)
