# solution1
def twoSum(nums, target):
    # key->[7,2,3]
    # value->0,1,2 index of element
    values = {}
    # idx = 0,1,2
    # value = [7,2,3]
    for idx, value in enumerate(nums):
        # if 9-7=2 in values={7: 0, 2: 1, 3: 2}
        # check key in dict.
        # 7 is key
        if target - value in values:
            # return value in dict
            return [values[target - value], idx]
        else:
            values[value] = idx


nums = [7, 2, 3]
target = 9
print(twoSum(nums, target))


# solution2
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]


print(twoSum([2, 11, 7, 15], 9))
