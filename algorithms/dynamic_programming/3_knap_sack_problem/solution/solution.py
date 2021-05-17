
def knap_sack(x,items): #(value, weight) return maximum value
    items_tuple = items.items()
    sorted_items = sorted(items_tuple, key = lambda x: (-x[1][0]))
    max_value = 0

    for key, value in sorted_items:
        for key2, value2 in sorted_items[2:]:
            if value[1] + value2[1] <= x:
                x = x - (value[1] + value2[1])
                if max_value < value[0] + value2[0]:
                    max_value = value[0] + value2[0]
    return max_value
            
knap_sack(5, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}) == 8
knap_sack(5, {}) == 0
knap_sack(0, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}) == 0
knap_sack(5, {"hat": (2,2), "sunscreen": (3,2), "food": (4,4)}) == 5