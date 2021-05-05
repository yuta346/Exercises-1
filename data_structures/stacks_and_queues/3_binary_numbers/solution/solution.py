
def binary_numbers(n):
    queue = []
    for i in range(1,n+1):
        bin_num = bin(i).replace("0b", "")
        queue.append(bin_num)
    return queue

print(binary_numbers(5))