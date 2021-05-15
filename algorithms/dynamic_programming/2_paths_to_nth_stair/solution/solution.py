
def paths_nth_stair(n):

    dp = [1,1]
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])
    return dp[-1]



print(paths_nth_stair(3))