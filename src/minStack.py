"""
请设计一个栈，除了常规栈支持的pop与push函数以外，
还支持min函数，该函数返回栈元素中的最小值。
执行push、pop和min操作的时间复杂度必须为O(1)。


>>> Stack = MinStack()
>>> Stack.push(-2)
>>> Stack.push(0)
>>> Stack.push(-3)
>>> Stack.getMin()
-3

>>> Stack.pop()
>>> Stack.top()
0

>>> Stack.getMin()
-2

只是需要一个辅助栈，元素数量同步，但是维护顶部元素为栈的最小值
即可实现O(1)的效率
"""

import math


class MinStack:
    """docString placeholder"""

    def __init__(self):
        self.stack = []
        self.helperStack = [math.inf]

    def push(self, x):
        self.stack.append(x)
        self.helperStack.append(min(x, self.helperStack[-1]))

    def pop(self):
        self.stack.pop()
        self.helperStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.helperStack[-1]


myStack = MinStack()
myStack.push(-2)
myStack.push(0)
myStack.push(-3)

print(myStack.getMin())

myStack.pop()
print(myStack.top())

print(myStack.getMin())
