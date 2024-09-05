
print("Welcome to the favorite teachers program")


def display_teachers():
    print("\nYour favorite teachers ranked are: ", str(teachers))
    print("Your favorite teachers alphabetically are: ", sorted(teachers))
    print("Your favorite teachers alphabetically are: ", sorted(teachers, reverse=True))

    print("\nYour top two teachers are: " + teachers[0] + " and " + teachers[1])
    print("Your next two favorite teachers are: " + teachers[2] + " and " + teachers[3])
    print("Your least favorite teachers is: " + teachers[3])
    print("You have 4 favorite teachers")


teachers = []
teachers.append(input("\nWho is your first favorite teacher: ").title())
# teachers.append(teacher_1)
teachers.append(input("Who is your second favorite teacher: ").title())
teachers.append(input("Who is your third favorite teacher: ").title())
teachers.append(input("Who is your fourth favorite teacher: ").title())

#for i in range(1, 5):
 #   teacher = input(f"\nWho is your {i} favorite teacher: ").title()
  #  teachers.append(teacher)

display_teachers()

teachers.insert(0, input("\nOops, " + teachers[0] + " is no longer your favorite teacher. Please input a new teacher: ").title())

display_teachers()
# print("\nYour favorite teachers ranked are: ", str(teachers))
# print("Your favorite teachers alphabetically are: ", sorted(teachers))
# print("Your favorite teachers alphabetically are: ", sorted(teachers, reverse=True))
#
# print("\nYour top two teachers are: " + teachers[0] + " and " + teachers[1])
# print("Your next two favorite teachers are: " + teachers[2] + " and " + teachers[3])
# print("Your least favorite teachers is: " + teachers[3])
# print("You have 5 favorite teachers")

teachers.remove(input("\nWhat teacher would you like to remove: ").title())

display_teachers()




