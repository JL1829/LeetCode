"""
**test case**

>>> finder = MedianFinder()
>>> finder.addNum(1)
>>> finder.addNum(2)
>>> finder.findMedian()
1.5

>>> finder.addNum(3)
>>> finder.findMedian()
2
"""
import heapq


class MedianFinder:
    """Find the median in O(1) time"""

    def __init__(self):
        self.counter = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        self.counter += 1
        # as Python heap default is min heap
        # so pass in negative value to make it top
        heapq.heappush(self.max_heap, -num)
        # even number, pop the value to min heap
        max_heap_top_value = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top_value)

        if self.counter % 2 == 1:
            min_heap_top_value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top_value)

    def findMedian(self):
        if self.counter % 2 == 1:
            # odd number, then the median is the top value
            # of the heap
            return -self.max_heap[0]
        else:
            # as max heap return negative, so '-' is '+'
            return (self.min_heap[0] - self.max_heap[0]) / 2

    def __repr__(self):
        return f"Median Finder object with max heap: {self.max_heap}" \
               f"\n and min heap: {self.min_heap} "

    __str__ = __repr__


# another approach
class MedianFinder2:
    """placeholder"""

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if len(self.max_heap) == len(self.min_heap):
            # 先加到大顶堆，再把大顶堆元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            # 先加到小顶堆，再把小顶堆元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

    def __repr__(self):
        return f"Median Finder object with max heap: {self.max_heap}" \
               f"\n and min heap: {self.min_heap} "


if __name__ == '__main__':
    stream = MedianFinder()
    stream.addNum(1)
    stream.addNum(2)
    print(stream.findMedian())
    stream.addNum(3)
    print(stream.findMedian())

    stream2 = MedianFinder2()
    stream2.addNum(1)
    stream2.addNum(2)
    print(f"Approach 2: {stream2.findMedian()}")
    stream2.addNum(3)
    stream2.addNum(10)
    stream2.addNum(11)
    print(f"Approach 2: {stream2.findMedian()}")
