"""
在一个`n * m`的二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个**高效**的算法，输入一个这样的二维数组和一个整数，判断数组中是否有这个整数。

**例子**

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定`target = 3`, 返回`True`
给定`target = 20`, 返回`False`
"""


def findNumberIn2DArray(matrix, target):
    i = len(matrix) - 1
    j = 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
        elif matrix[i][j] == target:
            return True

    return False


if __name__ == '__main__':
    array = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(f"For the array: {array}\n, return {findNumberIn2DArray(matrix=array, target=3)}"
          f"\n For the array: {array}\n, return {findNumberIn2DArray(matrix=array, target=20)}")
