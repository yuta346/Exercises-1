
def min_max(lst):
    low = 0
    high = len(lst)-1
    max_int = float('-inf')
    min_int = float('inf')
    min_int, max_int  = _min_max(lst,low,high,max_int,min_int)
    return min_int,max_int

def _min_max(lst,low,high,max_int,min_int):
    if low == high:
        max_int = lst[low]
        min_int = lst[low]
        return min_int, max_int
    elif low == high-1:
        if lst[low]<lst[high]:
            max_int = lst[high]
            min_int = lst[low]
        else:
            max_int = lst[low]
            min_int = lst[high]
        return min_int, max_int
    else:
        mid = (low+high)//2
        min1,max1 = _min_max(lst,low,mid,max_int,min_int)
        min2,max2 = _min_max(lst,mid+1,high,max_int,min_int)

    return min(min1,min2), max(max1,max2)

print(min_max([8, 2, 1, 3, 1, 5])) == (1, 8)