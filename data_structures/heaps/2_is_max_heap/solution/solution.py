#completed
def is_max_heap(lst):
    for i in range(len(lst)//2-1):
        if lst[i]<lst[(2*i)+1]:
            print(lst[i], lst[(2*i)+1])
            return False
        if lst[i]<lst[(2*i)+2]:
            return False
    return True

print(is_max_heap([1, 2, 3, 7, 6, 4, 5])) == False
print(is_max_heap([5, 3, 4, 1, 2])) == True
# print(is_max_heap([])) == True