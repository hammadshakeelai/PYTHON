#Objective: Learn to store input in to variable,understand string concatenation and variable assignment
name = input("what is your name?")
print(name)

name="aleena"
print(name)

name ="jack"
print(name)

name=input("what is your name")
length=len(name)
print(length)

a=input()
b=input()

c=a
a=b
b=c
print ("a: " + a)
print("b: " + b)

print("welcome to the band name geneator:")
city=input("in which city you were born?\n")
pet=input("what is your pet name?\n")
band_name=city + " " + pet
print("your band name can be: " + band_name)