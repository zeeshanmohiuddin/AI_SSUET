text = input("Enter String: ")
copy = int(input("How many copies of String you need: "))

_str = text

for z in range(1,copy):
    text = text + _str 
print(text)
