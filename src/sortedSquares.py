"""
给定一个按非递减顺序的整数数组`A`， 返回每个数字的平方组成的新数组
要求也按照非递减顺序排序
Given a non-decrease sorted integer array: `A`, write an algorithm to return
it's square integer array, in non-decrease sorted

>>> A = [-4, -1, 0, 3, 10]
>>> sortedSquares(nums=A)
[0, 1, 9, 16, 100]

>>> A = [-7, -3, 2, 3, 11]
>>> sortedSquares(nums=A)
[4, 9, 9, 49, 121]
"""


def sortedSquares(nums: list) -> list:
    return sorted([i ** 2 for i in nums])


if __name__ == '__main__':
    print(sortedSquares(nums=[-4, -1, 0, 3, 10]))
    print(sortedSquares(nums=[-7, -3, 2, 3, 11]))
