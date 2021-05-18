# Feed Children

# Implement the function:

# def feed_children(cookies, children):
#     # your code here
# cookies and children are both lists of integers. The integers in cookies represent the size of a cookie, 
# the integers in children represent the hunger level of a child.

# A child can only be satisfied if they are given a cookie that has a size greater than or equal to their hunger level. 
# There are just as many cookies as children, and each child is to be given exactly one cookie.
# Return the maximum number of children that can be satisfied given the inputs. Sort both lists using the built-in sort, 
# then use a greedy algorithm to find an optimal cookie allocation.


def feed_children(cookies, children):

   max_num = 0
   cookies.sort()
   children.sort()
   cookie_ind = len(cookies)-1
   child_ind= len(children)-1
  
   while(cookie_ind >= 0 and child_ind >= 0 ):
       if(cookies[cookie_ind] >= children[child_ind]):
           max_num += 1
           cookie_ind -= 1
           child_ind -= 1
       else:
           child_ind -= 1
   return max_num

    # return len((set(cookies) & set(children))) 
    
cookies = [1,3,2,5,4]
children = [5,2,3,4,5]
print(feed_children(cookies, children))