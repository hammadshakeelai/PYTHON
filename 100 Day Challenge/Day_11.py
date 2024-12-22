#Objective make a random name selector

names = input("Enter the csv name text: ")
name_list = names.split(",")

import random

person_paying = random.choice(name_list)
print("The person to get their wallet empty is.....", person_paying)