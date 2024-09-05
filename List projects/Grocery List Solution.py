import datetime
from calendar import month
# create the datetime objects
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
# Welcome messages
# food and foods variables different, notice
foods = ["Meat", "Cheese"]
print("Welcome to the Grocery Store App")
print("Current date and time is " + month + "/" + day + "\t" + hour + ":" + minute)
print("You currently have " + foods[0] + " and " + foods[1] + " in your list.")
#get user input
food = input("\nEnter an item to add to grocery list:")
foods.append(food.title())
food = input("\nEnter an item to add to grocery list:")
foods.append(food.title())
food = input("\nEnter an item to add to grocery list:")
foods.append(food.title())

#print and sort the list
print("\nHere is your grocery list: ")
print(foods)
foods.sort()
print("Here is your grocery list sorted")
print(foods)

#simulate shopping
print("\nSimulating grocery shopping...")
print("\nCurrent grocery list..." + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list.")

print("\nCurrent grocery list..." + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list.")

print("\nCurrent grocery list..." + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list.")

#the store is out of an item...
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
no_items = foods.pop()
print("\nSorry, the store is out of " +no_items + ".")
new_food = input("What food would you like instead. ").title()
foods.insert(0, new_food)#insert needs two items, the index number and the variable)

print("\nHere is what is left in your list: ")
print(foods)