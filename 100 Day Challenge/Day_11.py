#Objective make a random name selector
num=2
if num==1:
    names = input("Enter the csv name text: ")
    name_list = names.split(",")

    import random

    person_paying = random.choice(name_list)
    print("The person to get their wallet empty is.....", person_paying)
elif num==2:
    names=input("enter the comma seperated names as text:  ")
    name_list=names.split(",")
    number_of_name=len(name_list)
    import random
    index_selected=random.randint(0,number_of_name-1)
    print(f"name that got choosen is {name_list[index_selected].strip()}.")
else:
    number_of_players=int(input("how many palyers are there: "))
    names_of_people=''
    for _ in range(number_of_players):
        name=input("enter name: ")
        names_of_people=names_of_people+','+name
    names_of_people.split(',')
    import random
    person_paying=random.choice(names_of_people)
    print(f'The person to get their wallet empty is.....{person_paying}')
    
####################################################################
#extra

my_list = [ "me" , "you" , "he" , "him" ]

my_list.append( "her" )    #use append to an a new item to the end of the string

my_list.extend( [ "his" , "she" , "mine" ] )     #use extend to extend the list with item from this list in extends input parameter
print( my_list )

my_new_list=  [ 'yes' , 'dop' , 'skibidi' ]
strange_list = [ my_list , my_new_list ]
print( strange_list )

#list.index("text object whose index you want")
my_list.index("me")