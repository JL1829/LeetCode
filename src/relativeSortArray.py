"""
给你两个数组：`arr1`, `arr2`

`arr2` 中的元素各不相同
`arr2` 中的元素都出现在`arr1`中

对`arr1` 的元素排序，按照`arr2`中的元素顺序

>>> ar1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
>>> ar2 = [2, 1, 4, 3, 9, 6]
>>> relativeSortArray(array1=ar1, array2=ar2)
[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

不要忘记Python sort函数是可以接受自定义key的
"""

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]


def relativeSortArray(array1, array2):
    def mycmp(x):
        return (0, rank[x]) if x in rank else (1, x)

    rank = {x: i for i, x in enumerate(array2)}
    array1.sort(key=mycmp)

    return array1


print(relativeSortArray(array1=arr1, array2=arr2))
