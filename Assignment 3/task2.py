# Ex : 2a
# Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

# Ex : 2b
# Start with the program you wrote for Exercise 2a.Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

# #*********************
person = {
    'first_name': 'Ali', 
    'last name': 'Asghar', 
    'age': 23,
    'city':'Karachi'
}

print(person.items())

#*********************************

people = [
    {
      'first_name': 'Ali', 
      'last_name': 'Asghar', 
      'age': 24,
      'city':'Karachi'
    },
    {
      'first_name': 'Hasan', 
      'last_name': 'sultan', 
      'age': 25,
      'city':'Karachi'
    },
    {
      'first_name': 'Saad', 
      'last_name': 'Rehan', 
      'age': 26,
      'city':'Karachi'
    }
]

for x in range(0,len(people)):
    print('First name: ',people[x]['first_name'])
    print('Last name: ',people[x]['last_name'])
    print('Age: ',people[x]['age'])
    print('City: ',people[x]['city'],'\n')
