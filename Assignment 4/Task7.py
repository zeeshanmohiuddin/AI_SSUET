lst = [12,10,5,6,52,36]
length = len(lst)
for i in range(0,2):
    temp = lst[0]
    for j in range(0,length-1):
        lst[j] = lst[j+1]
    lst[j+1] = temp
print(lst)