#Objective make a random name selector
num=2
if num%2==0:
    names = input("Enter the csv name text: ")
    name_list = names.split(",")

    import random

    person_paying = random.choice(name_list)
    print("The person to get their wallet empty is.....", person_paying)
else:
    number_of_players=int(input("how many palyers are there: "))
    names_of_people=''
    for _ in range(number_of_players):
        name=input("enter name: ")
        names_of_people=names_of_people+','+name
    names_of_people.split(',')
    import random
    person_paying=random.choice(names_of_people)
    print(f'The person to get their wallet empty is.....{person_paying}')