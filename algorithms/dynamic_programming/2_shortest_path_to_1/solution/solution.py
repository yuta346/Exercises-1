def shortest_path_to_1(n):

    dp = [None for x in range(n+1)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    if n == 1:
        return dp[1]
    if  n == 2 or n == 3:
        return dp[2]

    for i in range(4, n + 1):
        if dp[i] == None:
            if i%3 == 0 and 1 % 2 == 0:
                dp[i] = 1 + min(dp[i-1], dp[i//3], dp[i//2])
            elif i%3 == 0:
                dp[i] = 1 + min(dp[i-1], dp[i//3])
            elif i%2 == 0:
                dp[i] = 1 + min(dp[i-1], dp[i//2])
            else:
                dp[i] =1 + dp[i-1]
    return dp[n]

print(shortest_path_to_1(10))