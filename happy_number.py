# solution 1
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    terminal = {0, 1, 4, 16, 20, 37, 42, 58, 89, 145}
    while n not in terminal:
        n = sum(i * i for i in map(int, str(n)))
    return n == 1


print(isHappy(19))


# solution 2
def is_happy(n):
    def calculate_square_sum(num):
        result = 0
        while num > 0:
            digit = num % 10
            result += digit * digit
            num //= 10
        return result

    def is_happy_recursive(num, seen):
        if num == 1:
            return True
        if num in seen:
            return False

        seen.add(num)
        next_num = calculate_square_sum(num)
        return is_happy_recursive(next_num, seen)

    return is_happy_recursive((n, set()))


# solution 3
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1


# solution 4
def isHappy(n):
    seen = set()
    su_m = 0
    if n < 0:
        return False
    while n != 1 and n not in seen:
        seen.add(n)
        for i in str(n):
            digit = int(i) ** 2
            su_m += digit
        n = su_m
    return n == 1


# Test the function
print(is_happy(19))  # Expected output: True
print(is_happy(2))  # Expected output: False
