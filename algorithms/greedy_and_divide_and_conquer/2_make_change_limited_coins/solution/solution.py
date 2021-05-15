
def make_change(amount, denominations):
    count = 0
    for coin in reversed(list(denominations)):
        while amount >=coin and denominations[coin]!=0:
            amount-=coin
            count+=1
            denominations[coin]-=1
    if amount == 0:
        return count
    else:
        return -1
denominations = {1: 5, 2: 1, 10: 5, 50: 3, 100: 1, 200: 1}
denominations1 = {1: 5, 2: 1, 10: 5, 50: 3, 100: 1, 200: 1}
denominations2 = {1: 5, 2: 1, 50: 3, 100: 1, 200: 1}
denominations3 = {1: 5, 2: 1, 5: 1, 10: 1, 20: 1, 50: 3}
denominations4 = {1: 5, 2: 1, 50: 3, 100: 1, 200: 1}

make_change(450, denominations1) == 5
make_change(10, denominations2) == -1
make_change(10, {}) == -1
make_change(305, denominations4) == 6
make_change(43, denominations3) == -1

print(make_change(450, denominations)) == 5