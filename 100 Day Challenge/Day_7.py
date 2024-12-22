#Objective: 1)make a bmi calculator use if elif else and operators
#           2)check if an year is a leap year or not
 
##################################################
print("Welcome to BMI Calculator")
height = float(input("Enter your 'Height' in 'Meters': "))
weight = float(input("Enter your 'Weight' in 'KiloGrams': "))
BMI = weight/height**2
print("Your BMI is",BMI)
if BMI<=18.5 :
    print("You are 'Under-Weight'")
elif BMI<=25 :
    print("You have 'Normal-Weight'")
elif BMI<=30 :
    print("You are 'Slightly Over-Weight'")
elif BMI<=35 :
    print("You are 'Obese'")
elif BMI>35:
    print("You are 'clinically-Obese'") 
    
##################################################
print("Welcome to Leap Year Checker")
year = int(input("Enter a Year: "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("It's a Leap Year")
        else:
            print("Not a Leap Year")    
    else:
        print("It's a Leap Year")
else:
    print("Not a leap Year") 