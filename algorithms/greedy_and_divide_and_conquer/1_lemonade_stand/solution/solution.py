def lemonade_change(customer_bills):
    register = 0
    change = 0
    five = 0
    for bill in customer_bills:
        if bill > 5:
            change = bill-5
            if change%5==0 and five==0:
                return False
            elif change <= register:
                register-=change
                register+=bill
                five-=1
            else:
                return False
        else:
            register+=bill
            five+=1
    return True

customer_bills = [5, 10, 5, 20]
print(lemonade_change(customer_bills)) == True
customer_bills = [5, 20, 10]
print(lemonade_change(customer_bills)) == False
print(lemonade_change([])) == True
print(lemonade_change([5, 20, 5, 20])) == False
print(lemonade_change([5])) == True
print(lemonade_change([10])) == False
print(lemonade_change([5, 10, 10, 20])) == False
