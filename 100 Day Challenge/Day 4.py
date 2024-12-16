#Objective: Learn data types and type conversion

#to print a single word through index numbers.
print("hello"[4])

#data types
#integer: numbers.
#float: decimal or point numbers.
#bollean: only two values/True or False.

#how to concatenate strings and integers.
name=len(input("name?")) 
#to find any data datatype.
print(type(name))
new=str(name)
print("your name has"+ " "+new +" ""characters")

#datatypes
a=123
print(type(a))

a=str(a)
print(type(a))

a=(70 +float(100))
print(type(a))


#task
two_numbers=input()                #it will take input
print(type(two_numbers))           #it will print the datatype of input.
first_digit=int(two_numbers[0])    #it will convert the datatype of first index.
print(type(first_digit))           #it will print the datatype of first index.
second_number=int(two_numbers[1])  #it will convert the datatype of second index.
print(type(second_number))         #it will print the datatype of second index.
print(first_digit+ second_number)  #it will print the sum of the input.

#BMI
height=input()
weight=input()
print(type(height))
height2=float(height)
weight2=int(weight)
BMI=weight2/(height2**height2)
print(BMI)