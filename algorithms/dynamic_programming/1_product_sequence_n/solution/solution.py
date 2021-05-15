

def product_sequence_n(n):    
    result = 1
    j = 0
    if n <= 1:
        return 1
    else:
        while n > 0:
            result *= n
            n-=2
    return result
        





print(product_sequence_n(4)) == 8
print(product_sequence_n(5)) == 15