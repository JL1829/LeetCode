"""
给定一个数组`nums`， 和滑动窗口的大小`k`， 请找出所有滑动窗口里的最大值

**test case**

>>> nums = [1, 3, -1, -3, 5, 3, 6, 7]
>>> k = 3
>>> maxSlidingWindow(array=nums, size=k)
[3, 3, 5, 5, 6, 7]

>>> nums = []
>>> k = 3
>>> maxSlidingWindow(array=nums, size=k)
[]

**解释**

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

# Solution
Simple two pointer method
"""


def maxSlidingWindow(array, size):
    n = len(array)
    i = 0
    ans = []
    while size <= n:
        ans.append(max(array[i:size]))
        i += 1
        size += 1

    return ans


if __name__ == '__main__':
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    print(maxSlidingWindow(array=nums1, size=3))
    nums2 = []
    print(maxSlidingWindow(array=nums2, size=3))
