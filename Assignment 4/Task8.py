list1 = [ 2, -7, 5, -64, -14 ]
pos = 0
neg = 0
for a in list1:
    if(a>0):
        pos+=1
    elif(a<0):
        neg+=1
print("Positive numbers: ",pos)
print("Negative numbers: ",neg)