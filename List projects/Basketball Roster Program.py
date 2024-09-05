
print("Welcome to the Basketball Roster Program ")

#create the roster by using a list and appening to that last, I did 3/4 of the work here :D
roster = []
pg = input("\nWho is your point guard: ").title()
roster.append(pg)
sg = input("Who is your shooting guard: ").title()
roster.append(sg)
sf = input("Who is your small forward: ").title()
roster.append(sf)
pf = input("Who is your power forward: ").title()
roster.append(pf)
ct = input("Who is your center: ").title()
roster.append(ct)

#here we print the roster with the list's index
print("\nYour starting 5 for the upcoming basketball season")

print("\tPoint guard:\t\t" + roster [0])
print("\tShooting guard:\t\t" + roster [1])
print("\tSmall Forward:\t\t" + roster [2])
print("\tPower Forward:\t\t" + roster [3])
print("\tCenter:  \t\t\t" + roster [4])

# a player is then injured, we must replace it in the list
print("\nOh no,", sg, "is injured")
print("Your roster now only has 4 players")
new_player = input("Who will take " + sg + "'s spot: ").title()
roster[1] = new_player

# we then re-print
print("\nYour starting 5 for the upcoming basketball season")

print("\tPoint guard:\t\t" + roster [0])
print("\tShooting guard:\t\t" + roster [1])
print("\tSmall Forward:\t\t" + roster [2])
print("\tPower Forward:\t\t" + roster [3])
print("\tCenter:  \t\t\t" + roster [4])

print("\nGood luck " + new_player + ", you'll do great")
print("Your roster now has 5 players")