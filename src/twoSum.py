"""
给定一个整数数组`nums` 和一个目标值`target`
找出数组中和为目标值的两个数，返回它们的索引，不能重复

**test case**
>>> nums = [2, 7, 11, 15]
>>> targetNumber = 9
>>> twoSum(array=nums, target=targetNumber)
[0, 1]

因为nums[0] + nums[1] = 2 + 7 = 9
"""


def twoSum(array, target):
    hashtable = {}
    for i, num in enumerate(array):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[array[i]] = i

    return []
