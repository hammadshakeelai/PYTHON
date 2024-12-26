#Objective: Learn How to format, use operators, f-string


#round 
print('print(round(10/3,3))')
print(round(10/3,3))   #,3 means that it will display 3 digits after decimal.

#flow division (will give the result in which datatype the values are.)
print('print(8//3)')
print(8//3)

#f-string 
#instead of converting each data we use f-string it concatenate different datatypes
print('f"string{int}"')
score=10
height=1.8
rate=True
print(f"your score is {score} your height is{height} youe winning rate is{rate}")
#this way you dont need to covert them to str using str()


#task
age=input("age? ")
age2=int(age)
years=(90-age2)
weeks=years*52
print("you have "+str(weeks)+" left.")

#tip calculator task
print("welcome to tip calculator")
print("what is your total bill? $")
bill=input("num1? ")
bill2=float(bill)
print("How much tip do you want to give 10,12,15?")
tip=input("tip? ")
tip2=int(tip)
print("In how many people the bill will split? ",end="")
people=input()
people2=int(people)
bill1=(tip2/100)*bill2
total_bill=bill2+bill1
bill_per_person=(total_bill/people2)

#################################################||
final_amount="{:.2f}".format(bill_per_person)####||   "{:.2f}".format(  number  )
#################################################||

print(f"Every Person Should Pay: ${final_amount}")


name = "hammad"
age = 24
print("My name is {} and I am {} years old.".format(name,age))