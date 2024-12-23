#Objective make a random name selector
num=2
if num%2==0:
    names = input("Enter the csv name text: ")
    name_list = names.split(",")

    import random

    person_paying = random.choice(name_list)
    print("The person to get their wallet empty is.....", person_paying)
else:
    number_of_players=3
    for 

