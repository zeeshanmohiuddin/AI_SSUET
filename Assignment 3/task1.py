# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# •	Use a loop to print the name of each river included in the dictionary.
# •	Use a loop to print the name of each country included in the dictionary.



river_country = {
    'nile' : 'egypt',
    'Volga': 'Russia',
    'Mississippi': 'United States'
}

for x in river_country.keys():
    print(x,"run through", river_country[x],"\n River: ",x,"\nLocation: ",river_country[x])
    
