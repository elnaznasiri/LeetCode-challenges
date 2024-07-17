# solution 1
def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 1:
        return False
    ans = 1
    div = 2
    while div ** 2 <= num:
        if num % div == 0:
            ans += div
            if div != num // div:
                ans += num // div
        div += 1
    return ans == num


# مثال‌ها
print(checkPerfectNumber(6))  # خروجی: True (چون 6 یک عدد کامل است)
print(checkPerfectNumber(28))  # خروجی: True (چون 28 یک عدد کامل است)
print(checkPerfectNumber(10))  # خروجی: False (چون 10 یک عدد کامل نیست)


# solution 2
def is_perfect_number(n):
    if n <= 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n


# solution 3
import math


def is_perfect_number(n):
    if n <= 1:
        return False
    sum_of_divisors = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                print(n // i)
                sum_of_divisors += n // i
    return sum_of_divisors == n


print(is_perfect_number(6))  # خروجی: True (چون 6 یک عدد کامل است)
