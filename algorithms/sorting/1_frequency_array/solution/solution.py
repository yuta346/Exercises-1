
def frequency_array(lst):
    if not lst: return []
    temp = [0]*(max(lst)+1)
    lst_dict = {x:0 for x in list(lst)}
    for i in lst:
        lst_dict[i]+=1
        temp[i]=lst_dict[i]
    return temp


lst = [1, 1, 3, 4, 4, 5, 6, 8, 8, 8, 9]
frequency_array(lst) == [0, 2, 0, 1, 2, 1, 1, 0, 3, 1]