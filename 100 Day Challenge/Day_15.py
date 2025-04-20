n_num=int(input("enter the max num of the even sum calculator: "))
answer=0
for i in range(0,n_num+1,2):
    answer+=i
print(f'sum of all even numbers till {n_num} is : {answer}')

###################################################################
#password generator
import random
password=''
my_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '[', ']', '|', '}', '{', '>', '<', '?', '/', '.', ',', ';', ':', '}','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '`', '"', '1','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password_length = input("enter length of password you want generated: ")
for _ in range( password_length ) :
    password += random.choice( my_list )
print(f'This Your Generated Password : {password}')