#Completed
from collections import deque
def postfix_eval(exp):
    queue = deque()
    result = 0
    if len(exp)==1:
        return int(exp)
    for i in exp:
        if i.isdigit():
            queue.append(i)
        elif queue:
            if i == '+':
                result = int(queue.popleft()) + int(queue.popleft())
            elif i == '-':
                result = int(queue.popleft()) - int(queue.popleft())
            elif i == '*':
                result = int(queue.popleft()) * int(queue.popleft())
            elif i == '/':
                result = int(queue.popleft()) / int(queue.popleft())
        if result != 0: 
            queue.insert(0,result)
    return result

exp = "123+*"
# exp = "1223+*/"
# print(postfix_eval("3134-*/"))
print(postfix_eval("2"))
# print(postfix_eval(exp))