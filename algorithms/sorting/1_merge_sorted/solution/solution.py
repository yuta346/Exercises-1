

def merge_sorted(lst1,lst2):
    left_len = len(lst1)
    right_len = len(lst2)
    i = j = k = 0
    temp = [0] * (len(lst1) + len(lst2))
    while i < left_len and j < right_len:
        if lst1[i] < lst2[j]:
            temp[k] = lst1[i]
            i += 1
        else:
            temp[k]=lst2[j]
            j += 1
        k += 1
    while i < left_len:
        temp[k] = lst1[i]
        i += 1
        k += 1
    while j < right_len:
        temp[k] = lst2[j]
        j += 1
        k += 1
    return temp

lst1 = [-1, 1, 4, 6]
lst2 = [0, 1, 2, 5, 7]
print(merge_sorted(lst1, lst2)) == [-1, 0, 1, 1, 2, 4, 5, 6, 7]