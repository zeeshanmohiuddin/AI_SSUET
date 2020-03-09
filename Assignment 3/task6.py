my_dict = {
    'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
    'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
    'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]
    }

print(my_dict)
print(my_dict['x'][4])
print(my_dict['y'][4])
print(my_dict['z'][4])

for a in my_dict.keys():
    print(a,'has value', my_dict[a])