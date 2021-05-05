#Completed
def minimum_parentheses(pstr):
    # count_open = 0
    # count_to_add = 0
    # for i in pstr:
    #     if i == '(':
    #         count_open+=1
    #     elif count_open >0:
    #         count_open-=1
    #     else:
    #         count_to_add+=1
    # return count_to_add + count_open

    stack = []
    for i in pstr:
        print(stack)
        if i == ')':
            if stack and stack[-1]=='(':
                stack.pop()
                continue
        stack.append(i)
    return len(stack)



            
        

        
pstr = "()))(("
print(minimum_parentheses(pstr))
# print(minimum_parentheses("()(()())") ) #0
# print(minimum_parentheses("()((")) #2
# print(minimum_parentheses("()))((()")) #== 4