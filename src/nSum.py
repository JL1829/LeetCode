"""
给定一个长度为n的整数列表nums, 求返回一个n元组，使得这n个数的和为target
n元组不得重复

例子：
>>> numbers = [1, 2, 3, 4, 5]
>>> target = 6
>>> n = 2
>>> nSum(array=numbers, n=n, start=0, target=target)
[[1, 5], [2, 4]]

>>> numbers = [-1, 0, 1, 2, -1, -4]
>>> target = 0
>>> n = 3
>>> nSum(array=numbers, n=n, start=0, target=target)
[[-1, 0, 1], [-1, -1, 2]]
"""

nums = [1, 2, 3, 4, 5]
targetNumber = 6


def nSum(array, n, start, target):
    array.sort()
    size = len(array)
    result = []
    if n < 2 or size < n:
        return result
    if n == 2:
        low = start
        high = size - 1
        while low < high:
            total = array[low] + array[high]
            left = array[low]
            right = array[high]
            if total < target:
                while low < high and array[low] == left:
                    low += 1
            elif total > target:
                while low < high and array[high] == right:
                    high -= 1
            else:
                result.append([left, right])
                while low < high and array[low] == left:
                    low += 1
                while low < high and array[high] == right:
                    high -= 1
    else:
        for i in range(start, size):
            sub = nSum(array, n - 1, i + 1, target-array[i])
            for arr in sub:
                arr.append(array[i])
                result.append(arr)
            while i < size - 1 and array[i] == array[i + 1]:
                i += 1

    return result


print(nSum(array=nums, n=2, start=0, target=targetNumber))
