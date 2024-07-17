#solution 1
def add_digits(num):
    while num >= 10:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        num = sum_digits
    return num

# solution 2
def add_digits(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

#solution 3
def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    return (num - 1) % 9 + 1 if num > 0 else 0