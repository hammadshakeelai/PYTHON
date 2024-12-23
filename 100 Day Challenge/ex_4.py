#Objective use memoiaztion to find last number from fibonaaci sequence
#is suppose to be really fast
def fibonacci(n):
    memo={}
    for i in range(1,n+1):
        if i == 1 :
            result = 0
        elif i==2:
            result=1
        else: 
            result = memo[i-1] + memo[i-2]
        memo[i]=result
    return memo[n]
print(fibonacci(9998))


# def factorial(n):
#     memo = {}
#     for i in range(1, n + 1):
#         if i == 1:
#             result = 1
#         else:
#             result = i * memo[i-1]
#         memo[i] = result
#     return memo[n]

# print(factorial(5))
