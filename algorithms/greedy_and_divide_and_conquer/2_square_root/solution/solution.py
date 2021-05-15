
def bin_sqrt(n):
    if n < 2:
        return n
    start = 0
    end = n-1
    result = 0

    while start <= end:
        mid = (start+end)//2
        if mid*mid == n:
            return mid
        elif mid*mid < n:
            start = mid+1
            result = mid
        else:
            end = mid-1

    return result

