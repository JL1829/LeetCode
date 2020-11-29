"""
给定一个以字符串表示的非负整数`num`, 移除这个数中的 k 位数字，使得剩下
的数字最小

**注意**
* num 的长度小于10002 且 > k
* num 不会包含任何前置0

**Test Case**
>>> num = '1432219'
>>> k = 3
>>> removeKdigits(numbers=num, target=k)
'1219'

>>> num = '10200'
>>> k = 1
>>> removeKdigits(numbers=num, target=k)
'200'

>>> num = '10'
>>> k = 2
>>> removeKdigits(numbers=num, target=k)
'0'
"""


def removeKdigits(numbers, target):
    stack = []
    remain = len(numbers) - target
    for digit in numbers:
        while target and stack and stack[-1] > digit:
            stack.pop()
            target -= 1
        stack.append(digit)
    return ''.join(stack[:remain]).lstrip('0') or '0'


num1 = '1432219'
num2 = '10200'
num3 = '10'
k1 = 3
k2 = 1
k3 = 2

print(f"For number: {num1} with target: {k1}"
      f" The min output is {removeKdigits(numbers=num1, target=k1)}")
print(f"For number: {num2} with target: {k2}"
      f" The min output is {removeKdigits(numbers=num2, target=k2)}")
print(f"For number: {num3} with target: {k3}"
      f" The min output is {removeKdigits(numbers=num3, target=k3)}")
