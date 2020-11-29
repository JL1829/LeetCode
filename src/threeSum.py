"""
给你一个包含n个整数的数组：nums, 判断nums是否存在三个元素：
a, b, c
使得a + b + c == 0

找出所有满足条件的三元组
**三元组不可重复**

>>> numbers = [-1, 0, 1, 2, -1, -4]
>>> three_sum(array=numbers)
[[-1, -1, 2], [-1, 0, 1]]
"""

nums = [-1, 0, 1, 2, -1, -4]


def three_sum(array):
    array.sort()
    result = []
    for k in range(len(array) - 2):
        if array[k] > 0:
            # as j > i > j
            break
        if k > 0 and array[k] == array[k - 1]:
            # skip the same `array[k]`
            continue
        i = k + 1
        j = len(array) - 1
        while i < j:
            s = array[k] + array[i] + array[j]
            if s < 0:
                i += 1
                while i < j and array[i] == array[i - 1]:
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and array[j] == array[j + 1]:
                    j -= 1
            else:
                result.append([array[k], array[i], array[j]])
                i += 1
                j -= 1
                while i < j and array[i] == array[i - 1]:
                    i += 1
                while i < j and array[j] == array[j + 1]:
                    i -= 1

    return result


print(f"For input array nums: {nums}, 3 sum output is: "
      f"\n {three_sum(array=nums)}")
