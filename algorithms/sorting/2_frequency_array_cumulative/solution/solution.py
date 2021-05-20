def frequency_array_cumulative(lst):
    lstsorted = frequency_array(lst)
    if len(lstsorted)==1:
        return lstsorted
    temp = [0]*len(lstsorted)
    for i in range(1, len(lstsorted)):
        temp[i] = lstsorted[i] + temp[i-1]
    return temp

def frequency_array(lst):
    if not lst: return []
    temp = [0]*(max(lst)+1)
    for i in lst:
        temp[i] = temp[i]+1
    return temp


# lst = [1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6]
# print(frequency_array_cumulative(lst))
# print(frequency_array_cumulative([])) == []
print(frequency_array_cumulative([0])) == [1]
# print(frequency_array_cumulative([1])) == [0, 1]
# print(frequency_array_cumulative([3])) == [0, 0, 0, 1]
# print(frequency_array_cumulative([1, 1, 2, 3, 3, 3, 5, 8, 8])) == [0, 2, 3, 6, 6, 7, 7, 7, 9]
print(frequency_array_cumulative([1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6])) == [0, 2, 2, 3, 5, 6, 7, 7, 10, 11]

