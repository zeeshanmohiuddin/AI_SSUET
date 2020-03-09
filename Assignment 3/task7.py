# Ex : 7a
# Create a new dictionary called prices
# •	Put these values in your prices dictionary: "banana": 4, "apple": 2, "orange": 1.5, "pear": 3
# •	Loop through each key in prices. For each key, print out the key along with its price
# •	Check whether the topping is in the list . If yes , Recall the order else ask for another one

# Ex : 7b
# Let's determine how much money you would make if you sold all of your food.
# •	Create a variable called total and set it to zero.
# •	Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock.
# •	Print that value into the console and then add it to total.
# •	Finally, outside your loop, print total.


prices = {
    "banana": 4, 
    "apple": 2, 
    "orange": 1.5, 
    "pear": 3
}

stock = {
    "banana": 1, 
    "apple": 2, 
    "orange": 4, 
    "pear": 3
}

total = 0
loop_control = 0
sum_list = []

# for x in prices:
#     print(x,":",prices[x])

# while loop_control == 0:
#     topping = input("Add Topping you want: ")
#     if topping in prices.keys():
#         print("Your order is: ",topping, " and price is : ",prices[topping])
#         loop_control=1
#     else:
#         print("Place another order")


for y in prices:
    print(y,":",prices[y]*stock[y])
    sum_list.append(prices[y]*stock[y]) 

total = sum(sum_list)
print("Total: ",total)
    