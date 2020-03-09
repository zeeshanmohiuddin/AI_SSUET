# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
# OUTPUT
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}


dict4 = {
    
}


for x,y,z in zip(dic1.keys(),dic2.keys(),dic3.keys()):
    dict4[x] = dic1[x]
    dict4[y] = dic2[y]
    dict4[z] = dic3[z]

print(dict4) 