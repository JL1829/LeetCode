"""
给定一个矩阵`A` 返回`A`的转置矩阵

矩阵的转置是指将主对角线翻转，交换矩阵的行索引和列索引。

**test case**
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> transpose(array=matrix)
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> transpose(array=matrix)
[[1, 4], [2, 5], [3, 6]]

# Solution
shape 为 R x C 的矩阵A 转置后会得到shape 为 `C x R`的矩阵`answer`, 对此
有`answer[c][r] = A[r][c]`

初始化一个新的矩阵`answer`, 赋值为全`None`, 把转置后的矩阵复制其中。

时间复杂度： $O(R * C)$
空间复杂度： $O(R * C)$， 由于需要初始化一个新的矩阵`answer`
"""


def transpose(array):
    ROW, COL = len(array), len(array[0])
    answer = [[None] * ROW for _ in range(COL)]

    for r, row in enumerate(array):
        for c, value in enumerate(row):
            answer[c][r] = value

    return answer


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(array=matrix))
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(transpose(array=matrix))
