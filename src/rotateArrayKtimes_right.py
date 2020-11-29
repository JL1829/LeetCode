"""
给定一个数组，将数组中的元素向右移动`k`个位置

* 时间复杂度没有限制
* 空间复杂度不可以大于$O(1)$

**test case**
>>> A = [1, 2, 3, 4, 5, 6, 7]
>>> rotateArray(array=A, k=3)
[5, 6, 7, 1, 2, 3, 4]

>>> A = [-1, -100, 3, 99]
>>> rotateArray(array=A, k=2)
[3, 99, -1, -100]

>>> A = [1, 2, 3, 4, 5, 6, 7]
>>> rotateArray_2(array=A, k=3)
[5, 6, 7, 1, 2, 3, 4]

>>> A = [-1, -100, 3, 99]
>>> rotateArray_2(array=A, k=2)
[3, 99, -1, -100]

# Solution
由于空间复杂度限制，使用三次翻转法
"""


# first approach
def rotateArray(array, k):
    if not array:
        return []

    left = 0
    right = len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    left = 0
    right = k - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    left = k
    right = len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array


"""
If you found your code repeated many times,
then is time to write a function for it
"""


# 2nd approach
def rotateArray_2(array, k):
    if not array:
        return []

    def reverse(receiveArr, start_index, end_index):
        while start_index < end_index:
            receiveArr[start_index], receiveArr[end_index] = receiveArr[end_index], receiveArr[start_index]
            start_index += 1
            end_index -= 1

    k = k % len(array)
    reverse(receiveArr=array, start_index=0, end_index=len(array) - 1)
    reverse(receiveArr=array, start_index=0, end_index=k - 1)
    reverse(receiveArr=array, start_index=k, end_index=len(array) - 1)

    return array
