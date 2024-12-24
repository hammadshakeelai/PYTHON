import random,time
print("welcome to rock paper scissor game")
print("Choices: 0 for Rock, 1 for Paper, 2 for Scissor")
choice=int(input("Enter Your Choice:  "))
my_list=[0,1,2]
while choice not in my_list:
    choice=int(input("Enter Your Choice:  "))
    time.sleep(.2)
choices=['rock','paper','scissor']
comp_choice=random.randint(0,2)
time.sleep(.5)
print("Processing...")
time.sleep(.5)

print(f"You chose {choices[choice]}. Computer chose {choices[comp_choice]}.")
time.sleep(.5)
print("Processing...")
time.sleep(.5)

if choice==comp_choice:
    print("It's a Draw.")
elif choice==0 and comp_choice==2 or choice==1 and comp_choice==0 or choice==2 and comp_choice==1:
    print("You Won!.")
else:
    print("Computer Won.")