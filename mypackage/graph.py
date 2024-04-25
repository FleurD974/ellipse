import numpy as np
import matplotlib.pyplot as plt
from mypackage import search

#function to show and compare informations about cities
def show_info_cities():
  cities = np.array(['amiens', 'cergy-pontoise', 'creteil', 'lyon', 'marseille', 'mulhouse','nancy','nantes','rouen', 'toulouse'])
  infos = np.array(search.city_infos(cities))
  total_stations = infos[0]
  total_bikes = infos[1]
  fig, (ax1, ax2) = plt.subplots(2,1, figsize= (12,4))
  ax1.bar(cities, total_stations, label='Nombre de station')
  ax1.legend()
  ax2.bar(cities, total_bikes, label='Nombre de vélo')
  ax2.legend()
  fig.suptitle("Comparaison du nombre de station (en haut) et vélos (en bas) dans les villes de France.")
  plt.show()
  