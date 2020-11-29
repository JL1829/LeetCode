"""
给定一个排序数组，你需要在**原地**删除重复出现的元素，使得每个元素只出现一次
返回移除后数组的新长度

**必须原地修改数组**
**空间复杂度必须为O(1)**

**test case**
>>> nums = [1, 1, 2]
>>> removeDuplicate(nums)
2

>>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
>>> removeDuplicate(nums)
5

## Approach one:
if there's no limitation about O(1) space, the solution could be
simple: just use set()

>>> nums = [1, 1, 2]
>>> removeDuplicate_set(nums)
2

>>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
>>> removeDuplicate_set(nums)
5

## Appproach two:
But there's limitation on space: O(1), and modify the array in-place.
we have to use two pointer:

define nums[0...i] is the non-duplicate array, and maintain this
while traversal the array
"""


def removeDuplicate_set(array):
    return len(set(array))


def removeDuplicate(array):
    n = len(array)
    if n == 0 or n == 1:
        return n

    # two pointer
    i = 0
    j = i + 1
    while j <= n - 1:
        if array[j] != array[i]:
            # 下一个不重复的元素，或者不是current 元素的下一个
            if i + 1 != j:
                # 如果不是，将下一个元素变成第一个不同的
                array[i + 1] = array[j]
            i += 1
        # 为的是找到下一个不重复的元素
        j += 1
    return i + 1
    # 如果要原地返回无重复子数组，只需要
    # return array[:i]


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"With input array: {nums1},"
          f"\n non duplicate length is {removeDuplicate(nums1)}")
    print(f"\n With input array: {nums2}"
          f"\n non duplicate length is {removeDuplicate(nums2)}")
