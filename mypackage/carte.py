import folium
import folium.map
from folium.plugins import MarkerCluster

#show the station of a french city on a map
def show_city_map(data: list):
  lat = data[0]['position']['lat']
  long = data[0]['position']['lng']
  my_map = folium.Map(location=(lat, long), zoom_start=13, control_scale=True)
  for i in range(len(data)):
    lat_station = data[i]['position']['lat']
    lng_station = data[i]['position']['lng']
    state = data[i]['status']
    available_bike = data[i]['available_bikes']
    available_place = data[i]['available_bike_stands']
    popup = f'La station est {state}, il y a {available_bike} vélos disponibles et {available_place} places disponibles'
    folium.Marker(location=[lat_station, lng_station],
                  tooltip="Cliquer pour plus d'informations",
                  popup=popup,
                  icon=folium.Icon(color="green", icon="bicycle", prefix="fa"),).add_to(my_map)
  my_map.save("./index.html")

