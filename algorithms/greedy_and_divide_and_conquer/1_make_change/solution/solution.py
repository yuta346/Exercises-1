

def make_change(amount,denominations):
    count = 0
    for coin in reversed(denominations):
        while amount >= coin:
            amount-= coin
            count+=1
    if amount ==0:
        return count
    return -1

denominations = [1, 2, 5, 10, 20, 50, 100, 200]
denominations1 = [1, 2, 5, 10, 20, 50, 100, 200]
denominations2 = [1, 2, 5, 100]
denominations3 = [20, 50, 100, 200]
denominations4 = [1, 100, 200]

print(make_change(50, denominations1)) == 1
print(make_change(233, denominations2)) == 10
print(make_change(30, denominations3))== -1
print(make_change(77, denominations4)) == 77
print(make_change(450, denominations)) == 3