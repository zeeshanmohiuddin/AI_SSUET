string = input("Enter any string: ")
string = string.casefold()
String = string[::-1]
if string==String:
    print("It is a Palindrome!")
else:
    print("It is not a Palindrome")