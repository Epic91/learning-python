# Your code below:
#
# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.
# Create a list that holds pizza toppings
toppings = ["pepperoni", "pineapple" ,"cheese", "sausage", "olives", "anchovies",
"mushrooms"]

# Create a list of pizza prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Count num of occurances of 2 in prices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find len of toppings
num_pizzas = len(toppings)
print(num_pizzas)

# Use concatination
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Create 2D list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
# print(pizza_and_prices)

# sort list ascending in price
pizza_and_prices.sort()
# print(pizza_and_prices)

# first el in list
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# priciest pizza
priciest_pizza = pizza_and_prices[-1]
# print(priciest_pizza)

# remove priciest slice
pizza_and_prices.pop()

# add new sub list to list make sure to position it relative to the rest of the sorted data 
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Slice 3 pizzas
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)