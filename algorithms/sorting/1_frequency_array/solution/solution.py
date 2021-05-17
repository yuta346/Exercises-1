
def frequency_array(lst):
    if not lst: return []
    temp = [0]*(max(lst)+1)
    for i in lst:
        temp[i] = temp[i]+1
    return temp


lst = [1, 1, 3, 4, 4, 5, 6, 8, 8, 8, 9]
print(frequency_array(lst)) == [0, 2, 0, 1, 2, 1, 1, 0, 3, 1]