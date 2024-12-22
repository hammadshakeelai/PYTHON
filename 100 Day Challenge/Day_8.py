#Objective: make an advanced rollercoaster age and price machine
#           pizza flavour selector
#           pizza love calculator and LEARN COUNT
#           pizza TRESURE ISLAND game
################################

print("Welcome To Roller Coaster Ride") 
height = float(input("What is your Height in Feets?  ")) 
if height >= 5.2: 
    print("You can Ride.") 
    age = int(input("What's Your Age?  ")) 
    if age < 12: 
        bill = 200
        print("Pay Rs-200") 
    elif age < 18: 
        bill = 300 
        print("Pay Rs-300") 
    else: 
        bill = 350 
        print("Pay Rs-350") 
    photo = input("do you Want Photo also, yes or no: ") 
    if photo.lower() == "yes" or photo.lower() == "y": 
        bill = bill + 69 
        print(f"Your Total Bill is Rs-{bill}") 
    else: 
        print(f"Pay Rs-{bill}") 
else: 
    print("You Can't Ride, Sorry!")
    
#################################

print("Welcome To Pizza Buzz")
menu = input("Menu\n1:Small Pizza ('s') ---- $15\n2:Medium Pizza ('m') -----$20\n3:Large Pizza ('l') ---- $25\n:")
if menu == 's' :
    bill=15
    peporoni = input("Add Peporonni For Small-Pizza\nPrice: $2\n (y or n)\n:")
    if peporoni == 'y':
        bill+=2
    elif peporoni == 'n':
        bill+=0
    else:
        print("Choose Correct Please")

elif menu == 'm':
    bill=20
    peporoni = input("Add Peporonni For Medium-Pizza\nPrice: $3\n (y or n)\n:")
    if peporoni == 'y':
        bill+=3
    elif peporoni == 'n':
        bill+=0
    else:
        print("Choose Correct Please")        
elif menu == 'l': 
    bill=25
    peporoni = input("Add Peporonni For Large-Pizza\nPrice: $3\n (y or n)\n:")
    if peporoni == 'y':
        bill+=3
    elif peporoni == 'n':
        bill+=0
    else:
        print("Choose Correct Please")
else:
    print("Please Choose Correct Size")
bill=bill
cheese = input("Cheese for any Pizza is for $1\n(y or n)\n:")
if cheese == 'y':
    bill+=1
elif cheese == 'n':
    bill+=0
else:
    print("Choose Correct Please")
print(f"Your Total Bill is ${bill}")  
  
###################################

print("Welcome to Love Calculator")
name_1 = input("Enter the name of the First Person: ")
name_2 = input("Enter the name of the Second Person: ")
both_names = name_1 + name_2
lower_case = both_names.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
digit_1 = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
digit_2 = l + o + v + e

total_score = str(digit_1) + str(digit_2)
total_score = int(total_score)
if total_score<10 or total_score>90:
    print(f"Your Score is {total_score}, You Go togeather like coke and Mentos") 
elif total_score>=40 and total_score<=50:
    print(f"Your Score is {total_score}, You are Alright Togeather")
else:
    print(f"Your Score is {total_score}") 

#########################################

print('"WELCOME TO TRESURE ISLAND"\n"Your Mission is to Find Tresure"')
direction = input('''You're at a Cross-Road. Where you want to go?\nType "left" or "right":\n''' )
if direction == 'right':
    print("Game-Over!")
elif direction == 'left':
    print("You come to lake.\nThere is an Island in the middle of the lake.")
    opt = input('Type "wait" to wait for a boat.\nType "swim" to swim across:\n')
    if opt == 'swim':
        print("Game-Over!")
    elif opt == "wait":
        print("You arrived at the Island Unharmed")
        door = input("There is a house with 3 doors.\n(1):red\n(2):yellow\n(3):blue:\n")
        if door == 'red':
            print("Game-Over!")
        elif door == 'yellow':
            print("You Win!")
        elif door == 'blue':
            print("Game-Over!")
        else:
            print("Please Choose Correct Option!!!")    
    else:
        print("Please Choose Correct Option!!!")           
else:
    print("Please Choose Correct Option!!!")

#note to self: add more endings and more choices, and make it so i can jump from one ending to another but dont repeated code


