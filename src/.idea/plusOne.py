"""
给定一个由**整数** 组成的**非空** 数组表示的非负整数， 在该数的基础上加一
最高位数字存放在数组首位， 数组中每个元素只储存单个数字。
你可以假设除了整数0以外，这个整数不会以零开头。

**test case**
>>> digits = [1, 2, 3]
>>> plusOne(array=digits)
[1, 2, 4]

>>> digits = [4, 3, 2, 1]
>>> plusOne(array=digits)
[4, 3, 2, 2]

>>> digits = [0]
>>> plusOne(array=digits)
[1]

>>> digits = [9, 9, 9]
>>> plusOne(array=digits)
[1, 0, 0, 0]
"""


def plusOne(array):
    newList = []
    while array and array[-1] == 9:
        array.pop()
        newList.append(0)
    if not array:
        return [1] + newList
    else:
        array[-1] += 1

    return array + newList


if __name__ == '__main__':
    array1 = [1, 2, 3]
    print(plusOne(array=array1))
    array2 = [4, 3, 2, 1]
    print(plusOne(array=array2))
    array3 = [0]
    print(plusOne(array=array3))
    array4 = [9, 9, 9]
    print(plusOne(array=array4))
