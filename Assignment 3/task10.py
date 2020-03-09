my_dict = {
    1: ['Samuel', 21, 'Data Structures'],
    2: ['Richie', 20, 'Machine Learning'],
    3: ['Lauren', 21, 'OOPS with java']
    }
print("Name     Age     Course")
for x in my_dict.keys():
    print(my_dict[x][0]," ", my_dict[x][1], " ", my_dict[x][2])

