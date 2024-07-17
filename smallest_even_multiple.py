# solution 1
def smallestEvenMultiple(n):
    """
    :type n: int
    :rtype: int
    """
    res = 2
    while True:
        if res % n == 0:
            return res
        res += 2


# solution 2
def smallest_even_multiple(n):
    if n > 0:
        if n % 2 == 0:
            return n
        else:
            return 2 * n
    else:
        raise ValueError("Input must be a positive integer.")


# solution 3
import math


# lcm() after python3.9
def smallestEvenMultiple(n: int):
    return math.lcm(2, n)


# solution 4
def smallestEvenMultiple(n: int):
    # odd=>GCD(a, b) = 1
    # even=>GCD(a, b) = 2
    # GCD(a, b) = GCD(b, a % b)
    return (2 * n) // math.gcd(2, n)


# solution 5
def gsd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gsd(a, b)


def smallestEvenMultiple(n):
    return lcm(2, n)
