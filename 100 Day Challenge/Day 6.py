#Objective: Learn how to use if, else statements.


print("rollercoster ride!")
height=int(input("what is your height in cm?"))
print(height)
if height >= 120:  #if height is equal to or greater than 120cm then if part will excute.
    print("you are allowed.")
else:               #if the height value is less than 120cm then else part will excute.
    print("you are not allowed.")


#task:to check the number is odd or even through if else statements.
num=int(input("enter the number you want to check: "))

if num%2==0:            #if the reminder is 0 the if statement will excute.
    print("number is even.")
else:                       #if the reminder is not 0 then else prt will excute.
    print("number is odd.")
