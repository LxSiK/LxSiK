dict = {
        'a':1, 
        'b':2, 
        'c':3,
        }

for key in dict:
    dict[key] += 1
dict[1] = 4
print(dict)
'''
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  info = {"country": country,
          "visits": visits,
          "cities":[list_of_cities]
         }
  travel_log.append(info)
  print(travel_log)



# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")



''''''
cidades_visitadas = ['Salvador', 'Prado', 'Itacaré', 'Aracaju','Recife', 'Maceió', 'João Pessoa']
estados_visitados = ['Bahia', 'Sergipe', 'Pernambuco', 'Alagoas', 'Paraíba']
roteiro_viagem = {estados_visitados[0]:{'Cidades visitadas:':cidades_visitadas[0:3],'total de cidades':len(cidades_visitadas)},  
                  estados_visitados[1]:cidades_visitadas[3],
                  estados_visitados[2]:cidades_visitadas[4],
                  estados_visitados[3]:cidades_visitadas[5],
                  estados_visitados[4]:cidades_visitadas[6],

}

print(roteiro_viagem)
''''''
paises_visitados = ['brasil', 'eua', 'canada']
lista_paises = ''
for pais in paises_visitados:
    lista_paises += pais
    print(pais)


roteiro_viagem = {'País': lista_paises}
print(roteiro_viagem)
'''