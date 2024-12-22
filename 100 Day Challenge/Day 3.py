#Objective: Learn to store input in to variable,understand string concatenation and variable assignment
p=4
if 2>p:
    name = input("what is your name? ")
    print(name)
    print()
    name="shaheen afridi "
    print(name)
    print()
    name ="jack"
    print(name)
    print()
    name=input("what is your name? ")
    length=len(name)
    print(length)

    a=input('a? ')
    b=input('b? ')

    c=a
    a=b
    b=c
    print ("a: " + a)
    print("b: " + b)
    print()
print("welcome to the band name geneator:")
city=input("in which city you were born?\n")
pet=input("what is your pet name?\n")
band_name="x"+city[1:] + " " + pet
print("your band name can be: " + band_name)