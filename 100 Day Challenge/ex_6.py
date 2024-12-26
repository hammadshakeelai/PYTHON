#https://www.youtube.com/watch?v=ngCos392W4w
# def grid_paths(n, m):
#     if n==1 or m==1:
#         return 1
#     else:
#         return grid_paths(n-1, m)+grid_paths(n, m-1)
# print(grid_paths(4, 5))
# #########################################
# memo={}
# def grid_paths(n, m):
#     if (n,m) in memo:
#         return memo[(n,m)]
#     if n==1 or m==1:
#         return 1
#     else:
#         memo[(n,m)]=grid_paths(n-1, m)+grid_paths(n, m-1)
#         return memo[(n,m)]
# print(grid_paths(785, 93))
#########################################
def grid_paths(n, m):
    memo = {}
    
    for i in range(1, n+1):
        memo[(i,1)] = 1
    for j in range(1, m+1):
        memo[(1, j)] = 1
    for i in range(2, n +1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
    return memo[(n, m)]
print(grid_paths(60975, 93))


