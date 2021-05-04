import math

def prime_factors(n):
    prime_factors = [1]
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i
    if n> 2:
        prime_factors.append(int(n))

    return list(set(prime_factors))

prime_factors(10) == [1, 2, 5]
print(prime_factors(4)) #== [1, 13]
