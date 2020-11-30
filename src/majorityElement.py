"""
数组中占比超过一半的元素称之为"主要元素"
给定一个数组，找到它的主要元素，若没有，则返回`-1`


**进阶**
找到一个时间复杂度为$O(n)$, 空间复杂度为$O(1)$的算法

**test case**

>>> array = [1, 2, 5, 9, 5, 9, 5, 5, 5]
>>> majorityElement(nums=array)
5

>>> array = [3, 2]
>>> majorityElement(nums=array)
-1

>>> array = [2, 2, 1, 1, 1, 2, 2]
>>> majorityElement(nums=array)
2

# Solution
## Approach 1: Counter(), Set(), and iterate.
Time: $O(n)$, Space: $O(n)$

## Approach 2: Moore Vote
"""
from collections import Counter


def majorityElement(nums):
    counter = Counter(nums)
    temp = list(set(nums))
    result = -1
    for item in temp:
        if counter[item] > len(nums) / 2:
            result = item
            break

    return result


if __name__ == '__main__':
    testArray = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    print(majorityElement(nums=testArray))
    testArray = [3, 2]
    print(majorityElement(nums=testArray))
    testArray = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums=testArray))
