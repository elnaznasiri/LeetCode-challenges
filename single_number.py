def single_number(num):
    result = 0
    for i in num:
        result ^= i
    return result

print(single_number([4,1,2,1,2]))