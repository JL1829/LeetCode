"""
给定一个数组`nums`, 编写一个函数将所有的`0` 移动到数组的末尾，同时保持非零元素的相对顺序

**test case**
>>> nums = [0, 1, 0, 3, 12]
>>> moveZeros(array=nums)
[1, 3, 12, 0, 0]

# Solution
简单双指针技巧
"""


def moveZeros(array):
    n = len(array)
    left = right = 0
    while right < n:
        if array[right] != 0:
            # swap the non zero element to the right
            array[left], array[right] = array[right], array[left]
            left += 1
        right += 1
    return array
