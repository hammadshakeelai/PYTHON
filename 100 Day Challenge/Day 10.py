#Objective: learn random


import random
def using_randint():
    number = random.randint(0,1)

    if number == 0:
        print("Heads")
    else:
        print("Tails")
# using_randint()

def using_choice():
    posiblities_list=['heads','tails']
    print(random.choice(posiblities_list))
using_choice()