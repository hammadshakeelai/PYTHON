#Objective: Learn recursion and use it
def main():
    nth_num=int(input('enter nth term:  '))
    print(factorial(nth_num))
def factorial(n):
    if n==0:
        return 'error'
    if n==1: 
        return 0
    elif n==2:
        return 1
    else:
        return factorial(n-1)+factorial(n-2)
if __name__=='__main__':
	main()
#slow as fuck