
def longest_common_subseq(str1, str2):
    if len(str1)==0 or len(str2)==0:
        return 0
    
    num_combination = [[0 for i in range(len(str2)+1)] for i in range(len(str2)+1)]
    

        

str1 = "abc"
str2 = "ahbgdc"
# str1 = "abcdabcf"
# str2 = "ecfdacagb"
print(longest_common_subseq(str1, str2)) == 4