#Completed
def squares_dict(n):
    dict = {x:x*x for x in range(1,n+1)}
    return dict

print(squares_dict(5))