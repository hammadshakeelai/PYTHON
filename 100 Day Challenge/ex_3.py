#Objective Learn and use memoization
memo={}
def main():
    nth_num=int(input('enter nth term:  '))
    print(factorial(nth_num))
def factorial(n):
    if n in memo:
        return memo[n]
    if n==1: 
        result= 0
    elif n==2:
        result= 1
    else:
        result=factorial(n-1)+factorial(n-2)
    memo[n]=result
    return result
if __name__=='__main__':
	main()
#fast as fuck
#maximum recursion depth is 999 idk why
# dynamic programming = recursion + meoization