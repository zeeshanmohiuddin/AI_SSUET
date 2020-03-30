num=int(input("Please Enter Number: "))
a = 0
b = 1
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(a)