#Completed
def postfix_eval(exp):
    queue = []
    result = 0
    if len(exp)==1:
        return int(exp)
    for i in exp:
        if i in "0123456789":
            queue.append(i)
        elif queue:
            if i == '+':
                result = int(queue.pop(0)) + int(queue.pop(0))
            elif i == '-':
                result = int(queue.pop(0)) - int(queue.pop(0))
            elif i == '*':
                result = int(queue.pop(0)) * int(queue.pop(0))
            elif i == '/':
                result = int(queue.pop(0)) / int(queue.pop(0))
        if result != 0: 
            queue.insert(0,result)
    return result

exp = "123+*"
# exp = "1223+*/"
# print(postfix_eval("3134-*/"))
print(postfix_eval("2"))
# print(postfix_eval(exp))