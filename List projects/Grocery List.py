import datetime

#greeting screen
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
print("Welcome to the Grocery Store List App")
print("It is currently " + month + "/" + day + "\t" + hour + ":" + minute)

#appening foods to list
foods = ["Meat", "Cheese"]
print("The current foods in your list are: " + foods[0] + ", " + foods[1])
food = input("What foods would you like to add: ").title()
foods.append(food)

food = input("What foods would you like to add: ").title()
foods.append(food)

food = input("What foods would you like to add: ").title()
foods.append(food)

#sort the list
print("\nHere is your grocery list: ")
print(foods)
foods.sort()
print("Here is your grocery list sorted: ")
print(foods)

#simulated shopping
print("\nSimulating shopping...")
print("\nCurrently " + str(len(foods)) + " items in your cart")
buy_food = input("What item was added to shopping cart: ").title()
foods.remove(buy_food)
print("Current shopping cart: ")
print(foods)

print("\nSimulating shopping...")
print("\nCurrently " + str(len(foods)) + " items in your cart")
buy_food = input("What item was added to shopping cart: ").title()
foods.remove(buy_food)
print("Current shopping cart: ")
print(foods)

print("\nSimulating shopping...")
print("\nCurrently " + str(len(foods)) + " items in your cart")
buy_food = input("What item was added to shopping cart: ").title()
foods.remove(buy_food)
print("\nCurrent shopping cart: ")
print(foods)

# simulating a missing item
no_items = foods.pop()
print("Meat is out of stock")
new_item = input("\nPlease input another item: ").title()
foods.insert(1, new_item)
print("\nThis is your current grocery list: ")
print(foods)
