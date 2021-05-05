
def backspace_compare(str1,str2):
    if len(str1)!=len(str2):
        return False
    stack1 = []
    stack2 = []
    
    for char in str1:
        if char == '#':
            if stack1:
                stack1.pop()
                continue
        stack1.append(char)

    for char in str2:
        if char =='#':
            if stack2:
                stack2.pop()
                continue
        stack2.append(char)
    
    return stack1 == stack2

str1 = "ab#c"
str2 = "ad#c"
print(backspace_compare(str1,str2))