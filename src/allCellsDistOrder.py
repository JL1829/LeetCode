"""
给出`R`行`C`列的矩阵，其中单元格的整数坐标是`(r, c)` 满足`0 <= r < R` 且`0 <= c < C`
另外，我们在该矩阵中给出了一个坐标为`(r0, c0)` 的单元格

返回矩阵中所有单元格的坐标，并按照`(r0, c0)`的距离从小到大的排序，其中，
两单元格`(r1, c1)` 和`(r2, c2)`之间的距离是曼哈顿距离： `| r1 - r2 | + |c1 - c2|`

**test case**

>>> R, C, r0, c0 = 1, 2, 0, 0
>>> allCellsDistOrder(R, C, r0, c0)
[[0, 0], [0, 1]]

>>> R, C, r0, c0 = 2, 2, 0, 1
>>> allCellsDistOrder(R, C, r0, c0)
[[0, 1], [0, 0], [1, 1], [1, 0]]

>>> R, C, r0, c0 = 2, 3, 1, 2
>>> allCellsDistOrder(R, C, r0, c0)
[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]

"""


def allCellsDistOrder(R, C, r0, c0):
    matrix = [[i, j] for i in range(R) for j in range(C)]
    matrix.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return matrix


# if __name__ == '__main__':
#     R, C, r0, c0 = 1, 2, 0, 0
#     print(allCellsDistOrder(R, C, r0, c0))
#     R, C, r0, c0 = 2, 2, 0, 1
#     print(allCellsDistOrder(R, C, r0, c0))
