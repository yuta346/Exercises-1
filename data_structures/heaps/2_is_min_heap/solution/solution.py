#completed
def is_min_heap(lst):
    if not lst:return True
    if lst[0]>min(lst):
        return False
    else:
        for i in range(len(lst)//2-1):
            print(i)
            if lst[i]>lst[(2*i)+1]:
                print(lst[i], lst[(2*i)+1])
                return False
            if lst[i]>lst[(2*i)+2]:
                return False
    return True

print(is_min_heap([1, 2, 3, 7, 6, 4, 5])) == True
# print(is_min_heap([5, 1])) == False
print(is_min_heap([])) == True