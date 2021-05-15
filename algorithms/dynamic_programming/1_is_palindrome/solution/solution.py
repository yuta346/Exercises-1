def is_palindrome(str):
    str_list = list(str)
    for char in str_list:
        if char == str_list[-1]:
            str_list.pop()
        else:
            return False
    return True

print(is_palindrome("racecar"))