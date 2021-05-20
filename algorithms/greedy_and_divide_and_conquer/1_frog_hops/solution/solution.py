
def min_hops_helper(max_units, target, river, num_hops):
    position = 0
    print(river)
    print(position, target)
    for i in range(max_units, 0, -1):
        if position + i <= target and river[position + i] == 1:
            num_hops += 1
            position += i
            return min_hops_helper(max_units, target-i, river[position:], num_hops)
    if position == target:
        return num_hops
    else:
        return -1


def min_hops(max_units, n, river):
    return min_hops_helper(max_units, n, river, 0)

print(min_hops(3, 7, [1, 0, 0, 1, 1, 0, 0, 1])) 