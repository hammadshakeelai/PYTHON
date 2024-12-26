n_num=int(input("enter the max num of the even sum calculator: "))
answer=0
for i in range(0,n_num+1,2):
    answer+=i
print(f'sum of all even numbers till {n_num} is : {answer}')

