## Problem Description 
# Given two binary values `x` and `y`, compute the following bitwise operations:

# 1.Bitwise XOR (^)
# 2.Bitwise right shift (>>)
# 3.Bitwise left Shift (<<)

# In the the **solution.py** file, create three variables `ans_xor`,`ans_rs` and `ans_ls` to store 
# the resulting values of `x` xor `y`, `x` right-shift `y` and `x` leftshift `y` respectively.




x = 0b1001
y = 0b0001

ans_xor = x ^ y
ans_rs = x>>y
ans_ls = x<<y

print(ans_rs)