def tribonacci(n):
    dp = [0,0,1]
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(3, n+1):
            dp.append(dp[i-3]+dp[i-2]+dp[i-1])
    return dp[-1]
print(tribonacci(1))
