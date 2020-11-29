"""
给定一个正整数`n`， 生成一个包含`1` 到$n^2$ 的所有元素，并且元素
按照顺时针顺序螺旋排列的正方形矩阵

**test case*

>>> number = 3
>>> generateMatrix(n=number)
[[1, 2, 3], [8, 9, 4], [7, 6, 5]]

>>> number = 4
>>> generateMatrix(n=number)
[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

>>> number = 0
>>> generateMatrix(n=number)
0

>>> number = 1
>>> generateMatrix(n=number)
1

# Solution

生成一个`n x n`的全`0` 矩阵`mat`, 随后模拟整个螺旋循环的过程

* 定义当前左右，上下的边界：`left, right, top, bottom`, 初始值`num = 1`
   迭代终止值：`target = n ** 2`
* `while number <= target` 始终按照left ---> right, top ---> bottom
   right ---> left, left ---> top 的顺序填入`number`
   * 并且: `number += 1`
   * 更新边界： `top += 1`, `right -= 1`, `bottom -= 1`
* 返回`mat`
"""


def generateMatrix(n):
    if n == 0 or n == 1:
        return n

    left = 0
    top = 0
    right = n - 1
    bottom = n - 1
    mat = [[0 for _ in range(n)] for _ in range(n)]

    num = 1
    target = n ** 2

    # be careful the "<=", if just "<" then the last element cannot fill
    while num <= target:
        for col in range(left, right + 1):
            mat[top][col] = num
            num += 1
        top += 1

        for row in range(top, bottom + 1):
            mat[row][right] = num
            num += 1
        right -= 1

        # be careful of this invert
        # 请注意倒序，如果right = len(array)
        # 调用array[right] 的时候会越界
        # 同理，如果left = 0， 倒序的时候并不会读0
        # 需要 left - 1 = -1, 才会读0 index
        for col in range(right, left - 1, -1):
            mat[bottom][col] = num
            num += 1
        bottom -= 1

        for row in range(bottom, top - 1, -1):
            mat[row][left] = num
            num += 1
        left += 1

    return mat


if __name__ == '__main__':
    number1 = 3
    number2 = 4
    number3 = 0
    number4 = 1
    print(f"For number: {number1}"
          f"\n Output matrix is: {generateMatrix(n=number1)}")
    print(f"For number: {number2}"
          f"\n Output matrix is: {generateMatrix(n=number2)}")
    print(f"For number: {number3}"
          f"\n Output matrix is: {generateMatrix(n=number3)}")
    print(f"For number: {number4}"
          f"\n Output matrix is: {generateMatrix(n=number4)}")
