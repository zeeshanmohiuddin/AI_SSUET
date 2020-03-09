# Ex : 3
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city
# and include the country that the city is in, its approximate population,
# and one fact about that city. The keys for each city’s dictionary should be something like country, population, 
# and fact. Print the name of each city 
# and all of the information you have stored about it.

cities = {
    'karachi' : {
        'country': 'Pakistan',
        'population' : 149100,
        'fact': 'City of light'
    },
    'Berlin' : {
        'country': 'Germany',
        'population' : 374800,
        'fact': 'Berlin has the largest train station in Europe'
    },
    'Washington DC': {
        'country': 'America',
        'population' : 633427,
        'fact': 'Washington DC is missing J street.'
    }
}

for x in cities.keys():
    print(x)
    print('Country: ',cities[x]['country'])
    print('Population = ',cities[x]['population'])
    print('Fact: ',cities[x]['fact'], '\n')