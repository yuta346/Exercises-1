
def knap_sack(x,items): #(value, weight) return maximum value
    sorted_items = sorted(items.items(), key = lambda x: (-x[1][0]))
    max_value = 0
    max_weight  = x
    for key, value in sorted_items:
        for key2, value2 in sorted_items[int(len(sorted_items)//2):]:
            if value[1] + value2[1] <= max_weight and key != key2:
                max_weight = max_weight - (value[1] + value2[1])
                if max_value < value[0] + value2[0]:
                    max_value = value[0] + value2[0]
    print(max_value)
    return max_value
            

knap_sack(5, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}) == 8
knap_sack(5, {}) == 0
knap_sack(0, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}) == 0
knap_sack(5, {"hat": (2,2), "sunscreen": (3,2), "food": (4,4)}) == 5 #value, weight


#[('food', (4, 4)), ('sunscreen', (3, 2)), ('hat', (2, 2))]