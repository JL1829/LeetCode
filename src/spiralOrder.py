"""
给定一个包含`m x n` 元素的矩阵（m行， n列），按照顺时针螺旋顺序
返回矩阵中的所有元素到列表

**test case**

```py
>>> inputMatrix = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
>>> spiralOrder(matrix=inputMatrix)
[1, 2, 3, 6, 9, 8, 7, 4, 5]

>>> inputMatrix = [[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]]
>>> spiralOrder(matrix=inputMatrix)
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

```

# Solution
***

按层模拟
1. 设定4个指针：top, left, bottom, right
2. 从左到右遍历上侧元素：从(top, left) --> (top, right)
3. 从上到下遍历右侧元素：从(top + 1, right) ---> (bottom, right)
4. 如果left < right and top < bottom, 则从右到左遍历下侧元素：
    ：(bottom, right - 1) ---> (bottom, left) 使用[-1]进行倒序
    以及从下到上遍历左侧元素：(bottom, left) ---> (top + 1, left)
5. left += 1, top += 1, right -= 1, bottom -= 1
    继续循环，直到left > right, top > bottom
"""


def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    order = []

    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1

    while left <= right and top <= bottom:
        # 左闭右开， 最后一个元素不算
        # left close right open, the last element not included
        for col in range(left, right + 1):
            order.append(matrix[top][col])

        # 从第二行开始
        for row in range(top + 1, bottom + 1):
            order.append(matrix[row][right])

        if left < right and top < bottom:
            # 从倒数第二列开始
            for col in range(right - 1, left, -1):
                order.append(matrix[bottom][col])

            for row in range(bottom, top, -1):
                order.append(matrix[row][left])

        left += 1
        top += 1
        right -= 1
        bottom -= 1

    return order


if __name__ == '__main__':
    inputMatrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    inputMatrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(f"With input matrix: {inputMatrix1}"
          f"\n Output order is: {spiralOrder(matrix=inputMatrix1)}")

    print(f"With input matrix: {inputMatrix2}"
          f"\n Output order is: {spiralOrder(matrix=inputMatrix2)}")
