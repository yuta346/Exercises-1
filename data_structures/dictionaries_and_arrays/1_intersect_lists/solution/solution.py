#Completed
def intersect_lists(lst1,lst2):
    # result = []
    # for i in lst1:
    #     for j in lst2:
    #         if i==j:
    #             result.append(i)
    # return result

    # return list(set(lst1) & set(lst2))

    return [x for x in lst1 if x in lst2]



lst1 = [1, "a", -2, 1.4]
lst2 = ["cat", 0.5, "a", 1, 2]
print(intersect_lists(lst1,lst2))