#Completed

# ## Problem Description
# Assume you are climbing a stair case and it takes `n` steps to reach to the top. 
# Each time you can either climb 1 or 2 steps.
# Write a recursive Python function named `count_ways` that consumes a number `steps`. 
# The function returns the number of distinct ways to climb to the top. Hint: Make sure you attempt 
# the question before trying this one!

# * For Example
# ```
# countways(4) == 5 # (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

def count_ways(steps):
    if steps==0:
        return 1
    elif steps==1:
        return 1
    else: return count_ways(steps-1) + count_ways(steps-2)
print(count_ways(100))


# def count_ways(steps):
#     dp = [1,1]
#     if steps==0:
#         return dp[0]
#     elif steps==1:
#         return dp[1]
#     else:
#         for i in range(2,steps+1):
#             dp.append(dp[i-1]+dp[i-2])
#     return dp[-1]
# print(count_ways(100))