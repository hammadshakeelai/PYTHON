from collections import defaultdict
#https://www.youtube.com/watch?v=Hdr64lKQ3e4

def how_many_ways(target_value: int, coins: list):
    memo = defaultdict(lambda _: 0)
    memo[0] = 1
    for i in range(1, target_value + 1):
        memo[i] = 0
        
        for coin in coins:
            remainder = i - coin
            if remainder < 0 :
                continue
            
            memo[i] = memo[i] + memo[remainder]
        
    return memo[target_value]
#unresolved