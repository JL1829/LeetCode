"""
给定一个含有n个正整数的数组和一个正整数s, 找出改数组中满足其和>= s 长度
的
**最小**
**连续**
**子数组**

并返回其长度
若不存在，返回0

>>> subString = 7
>>> numbers = [2, 3, 1, 2, 4, 3]
>>> minSubArrayLen_slidingWindow(subString, numbers)
2

因为最小，不重复，子数组为：[4, 3]
长度为2

>>> subString = 5
>>> numbers = [1, 2, 3, 4]
>>> minSubArrayLen_slidingWindow(subString, numbers)
2

最小不重复子数组为：[2, 3]
长度为2
"""
nums = [2, 3, 1, 2, 4, 3]
s = 7


# two pointer method
def minSubArrayLen_slidingWindow(sub, array):
    if not array:
        return 0

    n = len(array)
    answer = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += array[end]
        while total >= sub:
            answer = min(answer, end - start + 1)
            total -= array[start]
            start += 1
        end += 1

    return 0 if answer == n + 1 else answer


print(f"For input: {nums}, and target: {s}"
      f"\n The output: {minSubArrayLen_slidingWindow(sub=s, array=nums)}")
