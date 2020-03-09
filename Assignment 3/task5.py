# Ex : 5
# Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
# OUTPUT
# Sample string : 'Dictionaries'
# Expected output: {'D': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 1, 'a': 1, 'r': 1 , 'e' : 1 , 's' : 1}

word = 'Dictionaries'
dict_word = {}

for x in word:
    if x in dict_word:
        dict_word[x] += 1
    else:
        dict_word[x] = 1
print(word)
print(dict_word)


