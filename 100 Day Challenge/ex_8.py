#O(m*k)
# def minimum_coins(my_coins_list, target_amount):
#     if target_amount==0:
#         answer = 0
#     else:
#         answer = None
#         for coin in my_coins_list:
#             remainder = target_amount - coin
#             if remainder < 0:
#                 continue
#             answer = min_ignore_none(answer,minimum_coins(my_coins_list,remainder)+1)
#     return answer

#########################################################

# def minimum_coins(my_coins_list: list , target_amount: int,memo={}):
#     if target_amount in memo:
#         return memo[target_amount]
#     if target_amount==0:
#         answer = 0
#     else:
#         answer = None
#         for coin in my_coins_list:
#             remainder = target_amount - coin
#             if remainder < 0:
#                 continue
#             answer = min_ignore_none(answer,minimum_coins(my_coins_list,remainder)+1)
#     memo[target_amount] =answer
#     return answer

################################################################
def minimum_coins(my_coins_list: list, target_value:int) -> int:
    memo = {}
    memo[0] = 0
    for i in range(1,target_value+1):
        for coin in my_coins_list:
            remainder = i - coin 
            if remainder < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i),memo.get(remainder)+1)
    return memo[target_value]
def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

list1=[1,5,4]
print(minimum_coins(list1,13))