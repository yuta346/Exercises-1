#Completed
def inventory_price(idict):
    total = 0
    for val in idict.values():
        total += val[0]*val[1]
    return total


idict = {"hat": (20, 15.50), "tshirt": (50, 19.99), "jeans": (10, 69.55)}
print(inventory_price(idict)) #== 2005.0

