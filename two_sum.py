
def twoSum(nums, target):
    values = {}
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx


print(twoSum([2,11,7,15], 9))

