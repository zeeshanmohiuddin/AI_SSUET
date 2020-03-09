my_dict = {'a':1, 'b':-2, 'c':-3, 'd':7, 'e':0}
new_dict = {}
print(my_dict)

for x in my_dict.keys():
    if my_dict[x] >= 0:
        new_dict[x]= my_dict[x]

print(new_dict)




