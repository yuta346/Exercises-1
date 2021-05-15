

def binary_search(lst,x):
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high)//2
        if lst[mid]==x: return mid
        elif lst[mid]>x: high = mid-1
        else: low = mid+1
    return -1 

lst = [1, 2, 4, 5, 9, 10, 11]
print(binary_search(lst, 4)) == 1
print(binary_search(lst, 7)) == -1