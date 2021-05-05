
#Completed
def inorder_to_postorder(exp):
    arr = []
    queue = []
    for char in exp:
        if char not in ['+','*','-','%','/']:
            arr.append(char)
        else:
            queue.append(char)
    while queue:
        opr = queue.pop(0)
        arr.append(opr)
    return "".join(arr)

print(inorder_to_postorder("123+*"))