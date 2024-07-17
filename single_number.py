# solution 1
def single_number(num):
    result = 0
    for i in num:
        result ^= i
    return result


print(single_number([4, 1, 9, 1, 9]))


# solution 2
def single_number(nums):
    n = len(nums)  # 5
    for i in range(n):  # 0to4
        found_duplicate = False
        for j in range(n):  # 0to4
            if i != j and nums[i] == nums[j]:
                found_duplicate = True
                break
        if not found_duplicate:
            return nums[i]


print(single_number([4, 1, 9, 1, 9]))


# solution 3
def singleNumber(nums):
    total_sum = sum(nums)  # جمع کل اعداد آرایه
    print(set(nums))
    print(sum(set(nums)))
    unique_sum = sum(set(nums)) * 2  # جمع اعداد یکتا ضربدر 2 (چون هر کدام دو بار در جمع قرار گرفته‌اند)
    return unique_sum - total_sum  # عددی که تنها یک بار در آرایه ظاهر شده است


# مثال استفاده:
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # خروجی: 4
