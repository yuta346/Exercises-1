
def binary_numbers(n):
    queue = []
    result = []
    for i in range(1,n+1):
        bin_num = bin(i).replace("0b", "")
        queue.append(bin_num)
        result.append(queue.pop(0))
    return result

print(binary_numbers(10))