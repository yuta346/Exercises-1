def partition(arr,start,end):
    pivot_elm = arr[start]
    pivot_index = start
    while start < end:
        while start < len(arr) and arr[start] <= pivot_elm:
            start += 1
        while arr[end] > pivot_elm:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quick_sort(lst):
    _quick_sort(lst,0,len(lst)-1)
    return lst

def _quick_sort(lst,start,end):
    if start < end:
        pivot_index = partition(lst, start ,end)
        _quick_sort(lst, start, pivot_index-1)
        _quick_sort(lst, pivot_index + 1, end)

lst = [9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]
print(quick_sort(lst)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]