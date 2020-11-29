"""
编写一个函数，将以数组形式的字符串啊翻转

**test case**

>>> inputString = ['h', 'e', 'l', 'l', 'o']
>>> reverseString(string=inputString)
['o', 'l', 'l', 'e', 'h']

>>> inputString = ['H', 'a', 'n', 'n', 'a', 'h']
>>> reverseString(string=inputString)
['h', 'a', 'n', 'n', 'a', 'H']

# Solution
Simple Two pointer
"""


def reverseString(string):
    left = 0
    right = len(string) - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1

    return string
