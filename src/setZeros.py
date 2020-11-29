"""
编写一种算法，若m x n矩阵中某个元素为0，则将其所在的行，和列，的所有元素
重置成0

>>> input1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
>>> setZeros(matrix=input1)
[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

>>> input2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
>>> setZeros(matrix=input2)
[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

"""

matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def setZeros(matrix):
    if not matrix:
        return []

    # as single row or single col could have multiple zero
    # so in order to take out the duplicate
    # we use set()
    # the row going to be set zero
    rows = set()

    # the column going to be set zero
    cols = set()

    # find the 0 index
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # now set row to be zero
    for row in rows:
        matrix[row] = [0] * len(matrix[0])

    # now set column to be zero
    # careful about the index
    for col in cols:
        # vertical direction
        for i in range(len(matrix)):
            matrix[i][col] = 0

    return matrix


print(setZeros(matrix=matrix1))
print(setZeros(matrix=matrix2))
