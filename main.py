from mypackage import search
from mypackage import graph
from mypackage import carte

cities = ['Amiens', 'Cergy-pontoise', 'Creteil', 'Lyon', 'Marseille', 'Mulhouse','Nancy','Nantes','Rouen', 'Toulouse']
city = input("Choisissez une ville parmis: Amiens, Cergy-Pontoise, Creteil, Lyon, Marseille, Mulhouse, Nancy, Nantes, Rouen ou Toulouse.\n")
if city in cities:
  data = search.get_data(city)
  update = carte.show_city_map(data)
else:
  print("Choisissez une des villes indiquées (n'oubliez pas la majuscule)!")

graph.show_info_cities()
