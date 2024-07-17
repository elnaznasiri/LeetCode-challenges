# solution1
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits) - 1 - i))
    return [int(i) for i in str(num + 1)]


print(plusOne([1, 2, 3]))


# solution2
def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


print(plus_one([4, 3, 2, 9]))


# solution3
def plus_one(digits):
    n = len(digits)
    i = n - 1
    while i >= 0:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        i -= 1
    return [1] + digits


print(plus_one([9, 9, 9]))


# solution4
def plus_one(digits):
    num = int(''.join(map(str, digits)))
    num += 1  # 123
    return [int(x) for x in str(num)]


print(plus_one([1, 2, 3]))


# solution5
def plusOne(digits):
    return [int(x) for x in str(pow(int(''.join(map(str, digits))), 1) + 1)]


print(plusOne([1, 2, 4]))


# solution6
# [1,2,3]->[3,2,1]->+1->reverse->[1,2,4]
def plusOne(digits):
    digits = digits[::-1]
    one, i = 1, 0
    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(1)
            one = 0
        i += 1
    return digits[::-1]


print(plusOne([1, 2, 3]))
