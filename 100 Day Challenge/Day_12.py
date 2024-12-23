import time
print('''      a    b    c    d   \n1  [ 'o' ,'o' ,'o' ,'o' ]\n2  [ 'o' ,'o' ,'o' ,'o' ]\n3  [ 'o' ,'o' ,'o' ,'o' ]\n4  [ 'o' ,'o' ,'o' ,'o' ]\n''')
line1 = [ 'o' , 'o' , 'o' , 'o' ]
line2 = [ 'o' , 'o' , 'x' , 'o' ]
line3 = [ 'o' , 'o' , 'o' , 'o' ]
line4 = [ 'o' , 'o' , 'o' , 'o' ]
lines = [ line1 , line2 , line3 , line4 ]
print("Hiding Your Treasure! X marks the spot...")
time.sleep(.5)
print("3.....")
time.sleep(.8)
print("2....")
time.sleep(1)
print("1....")
time.sleep(1.2)

position_input=input("Enter which box do you'd choose:  ")
#############################################
# flag=0
# my_alphabets_to_number_dict={'a':0,'b':1,'c':2,'d':3}
# position_number1=my_alphabets_to_number_dict[position_input[0].lower()]
# position_number2=int(position_input[1])-1
# if lines[position_number2][position_number1]=='x':
#     print("YOU ************ guessed correctly against all odds")
#     print("unique ki bike apki hoi")
#     flag=1
# #############################################
# print(f"      a    b    c    d   \n1  {line1}\n2  {line2}\n3  {line3}\n4  {line4}")
# if not flag:
#     print("You Failed to guess correctly now your treasure shall forever be mine")
#                      ||

###############################################
my_list = ['a','b','c','d']
position_number1 = position_input[0].lower()
position_number1 = my_list.index(position_number1)
position_number2 = int(position_input[1])-1
treasure_value=lines[position_number2][position_number1]
if treasure_value=='x':
    print("you've guess correctly, Hooray!!!.")
else:
    print("you failed miserably even with the luck of gods\nyour ancestors died once more time after this instance")
###############################################
print(f"      a    b    c    d   \n1  {line1}\n2  {line2}\n3  {line3}\n4  {line4}")