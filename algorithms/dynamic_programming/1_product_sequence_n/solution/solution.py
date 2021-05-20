

# def product_sequence_n(n):    
#     result = 1
#     j = 0
#     if n <= 1:
#         return 1
#     else:
#         while n > 0:
#             result *= n
#             n-=2
#     return result

def product_sequence_n(n):  
    if n == 0 or n == 1:
        return 1
    else:
        return n * product_sequence_n(n-2)




print(product_sequence_n(4)) == 8
print(product_sequence_n(5)) == 15