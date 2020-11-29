"""
给定一个整数数组`nums`， 找到一个具有最大和的连续子数组
（最少包含一个元素），返回其最大和

>>> nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
>>> maxSubArray_dp1(nums)
6

因为连续子数组：[4, -1, 2, 1]的和最大，为6

>>> nums = [-1, 0, 1, 2]
>>> maxSubArray_dp1(nums)
3

因为连续子数组：[1, 2]的和最大，为3

>>> nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
>>> maxSubArray_dp2(nums)
6

>>> nums = [-1, 0, 1, 2]
>>> maxSubArray_dp2(nums)
3
"""

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
numbers2 = [-1, 0, 1, 2]


# Dynamic Programming(DP) approach 1
def maxSubArray_dp1(array):
    size = len(array)
    if size == 0:
        return 0

    dp = [0 for _ in range(size)]

    dp[0] = array[0]
    for i in range(1, size):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + array[i]
        else:
            dp[i] = array[i]

    return max(dp)


print(maxSubArray_dp1(array=numbers))
print(maxSubArray_dp1(array=numbers2))


# Dynamic Programming(DP) approach 2
def maxSubArray_dp2(array):
    n = len(array)
    if n == 0:
        return 0

    dp = [0 for _ in range(n)]

    dp[0] = array[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + array[i], array[i])

    return max(dp)


print(maxSubArray_dp2(array=numbers))
print(maxSubArray_dp2(array=numbers2))


# Dynamic Programming(DP) approach 3
def maxSubArray_dp3(array):
    n = len(array)
    if n == 0:
        return 0

    previous = array[0]
    result = previous
    for i in range(1, n):
        previous = max(array[i], previous + array[i])
        result = max(result, previous)

    return result


print(maxSubArray_dp3(array=numbers))
print(maxSubArray_dp3(array=numbers2))
