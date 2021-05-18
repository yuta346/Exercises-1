from collections import deque

# def binary_numbers(n):
#     queue = []
#     result = []
#     for i in range(1,n+1):
#         bin_num = bin(i).replace("0b", "")
#         queue.append(bin_num)
#         result.append(queue.pop(0))
#     return result

def binary_numbers(n):
    if n == 0:
        return [0]
    queue = deque()
    queue.append('1')
    bin_lst = []
    for i in range(n):
        bin_val = queue.popleft()
        print(bin_val)
        bin_lst.append(bin_val)
        queue.append(bin_val+'0')
        queue.append(bin_val+'1')
    return bin_lst

# print(binary_numbers(1))
print(binary_numbers(10))