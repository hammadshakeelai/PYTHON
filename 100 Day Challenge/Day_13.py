# find prime number
my_prime_list=[]
for i in range(12):
    if i==1 or i==0:
        continue
    prime=True
    for j in range(i-1):
        if j==1 or j==0:
            continue
        if i%j==0:
            prime=False
            break
    if prime:
        my_prime_list.append(i)
print(my_prime_list)
#two factor numbers
my_2facto_nums=[]
size=len(my_prime_list)
for i in range(size):
    if i==(size-1):
        continue
    for j in range(i+1,size):
        my_2facto_nums.append(my_prime_list[i]*my_prime_list[j])
print(my_2facto_nums)
my_list=[]
# import random
my_list_ofN=[ 15, 21, 33, 35, 55, 77]
# N=int(input('enter the N number: '))
# N=55
for N in my_list_ofN:
    print(f'number to get factorised: {N}')
    #N=P*Q
    G=8 #G should share no factors with N

    power=1

    while True:
        # print(power)#-----------------------
        if (G**power)%N==1:
            break
        power+=1
    # print(power)#-----------------------
#if power is odd go back to first method 
    #((G**power/2)+1)((G**power/2)-1)== mN
    # ( P *f1) * ( Q *f2) == mN
    my_list.append((G**(power/2))+1)
    # print(((G**power/2)+1))#------------------
    my_list.append((G**(power/2))-1)
    # print((G**power/2)-1)#----------------------
    #euclids algorithm
    for numerator in my_list:
        divisor=N
        while True:
            
            remainder=numerator%divisor
            if numerator%divisor == 0:
                print(f'factor : {divisor}')
                break
            numerator=divisor
            divisor=remainder
#pass under very specific condition but in all other fails
#objective successfully achieved