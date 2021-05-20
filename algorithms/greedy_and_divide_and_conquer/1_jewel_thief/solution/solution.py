
def steal_jewels(x, jewels):
    if len(jewels)==0:
        return 0
    max_value = 0
    sorted_jewels = sorted(jewels, key=lambda x: -x[1]/x[0])
    for weight, value in sorted_jewels:
        if weight == 0:
            return 0
        if x >= weight:
            x -= weight
            max_value += value
        else:
            fraction_value = value/weight
            max_value += fraction_value * x
            return max_value
    return max_value

jewels = [(1, 4), (2, 8), (3, 15), (9, 50)]
jewels1 = [(1, 4), (2, 8), (3, 15), (9, 50)]
jewels2 = [(1, 1)]
jewels3 = [(1, 1), (2, 8), (3, 15), (4,24)]
# steal_jewels(10, jewels) == 55
# steal_jewels(10, jewels1) == 55
# steal_jewels(10, []) == 0
steal_jewels(1, jewels2) == 1
steal_jewels(3, jewels2) == 1
# steal_jewels(3, jewels3) == 18














