"""
给定一个已按照**升序排列**的有序数组，找到两个数使得它们相加之和等于目标数
返回这两个数的index, 从1开始（不是从0开始）
"""
sample_numbers = [2, 7, 11, 15]


def twoSum(array, target):
    # assume the array already been sorted
    low, high = 0, len(array) - 1
    while low < high:
        result = array[low] + array[high]
        if result < target:
            low += 1
        elif result > target:
            high -= 1
        elif result == target:
            return [low + 1, high + 1]


print(f"For input array: {sample_numbers}, two sum answer: "
      f"\n {twoSum(array=sample_numbers, target=9)}")
