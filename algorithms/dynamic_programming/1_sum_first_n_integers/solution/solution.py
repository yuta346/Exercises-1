def sum_first_n(n):
    if n <= 1:
        return n
    result = 0
    j = 0
    while n > 0:
        result+=n
        n-=1
    return result




print(sum_first_n(2)) == 3
print(sum_first_n(5)) == 15