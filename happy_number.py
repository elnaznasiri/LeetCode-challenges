def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    terminal = { 0, 1, 4, 16, 20, 37, 42, 58, 89, 145 }
    while n not in terminal:
        n = sum(i * i for i in map(int, str(n)))
    return n == 1
print(isHappy(19))