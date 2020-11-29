"""
请定义一个队列并实现函数`max_value`得到队列里面的最大值，
要求函数`max_value`, `push_back`和`push_front`的均摊时间复杂度都是$O(1)$

若队列为空，`pop_front` 和`max_value` 需要返回`-1`
"""

# 以下解决方法为$O(n)$ 法
# 达到$O(1)$ 取最大值，需要两个队列，看MaxQueue2
from collections import deque


class MaxQueue:
    """docString"""

    def __init__(self):
        self.queue = deque()

    def max_value(self):
        if not self.queue:
            return -1

        return max(self.queue)

    def push_back(self, value):
        self.queue.append(value)

    def pop_front(self):
        if not self.queue:
            return -1

        return self.queue.popleft()


class MaxQueue2:
    """docString"""

    def __init__(self):
        self.queue = deque()
        self.sorted_queue = deque()

    def push_back(self, value):
        self.queue.append(value)

        # make sure the sorted queue head is the max value
        while self.sorted_queue and self.sorted_queue[-1] < value:
            self.sorted_queue.pop()

        self.sorted_queue.append(value)

    def max_value(self):
        if self.sorted_queue:
            return self.sorted_queue[0]
        else:
            return -1

    def pop_front(self):
        if not self.queue:
            return -1

        # get the left element
        result = self.queue.popleft()
        # make sure the queue sync
        if result == self.sorted_queue[0]:
            self.sorted_queue.popleft()

        return result


if __name__ == '__main__':
    queue = MaxQueue()
    queue.push_back(1)
    queue.push_back(2)
    queue.push_back(3)
    print(queue.max_value())
    print(queue.pop_front())

    queue2 = MaxQueue2()
    queue2.push_back(1)
    queue2.push_back(2)
    queue2.push_back(3)
    print(queue2.max_value())
    print(queue2.pop_front())
