# solution1
def twoSum(nums, target):
    # key->[7,2,3]
    # value->0,1,2
    values = {}
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx

nums = [7,2,3]
target=9
print(twoSum(nums, target))




# solution2
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if target == nums[i]+nums[j]:
                return [i,j]
print(twoSum([2,11,7,15], 9))
