"""
给定一个链表， **返回链表开始入环的第一个节点**， 若链表无环，则返回`None`

**说明**
* 不允许修改链表
* 使用$O(1)$的空间

**注意**
这个和`hasCycle`相比，更近一步：返回环的第一个节点， 而不是Bool 值
"""


class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node with value: {self.value}"


def detectCycle(node):
    fast = node
    slow = node

    while True:
        if not (fast and fast.next):
            return
        fast = fast.next.next
        slow = slow.next
        # fast and slow meet the first time
        # fast reset, and slow continue in the cycle
        if fast == slow:
            break
    # reset fast to the head
    fast = head
    # both in the cycle, if they meet, fast will be the entry of the cycle
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast


if __name__ == '__main__':
    head = ListNode(5)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node7 = ListNode(7)
    node1 = ListNode(1)
    node6 = ListNode(6)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node4 = ListNode(4)

    head.next = node3
    node3.next = node2
    node2.next = node7
    node7.next = node1
    node1.next = node6
    node6.next = node8
    node8.next = node9
    node9.next = node4
    node4.next = node1

    print(detectCycle(node=head))

    head2 = ListNode(-1)
    print(detectCycle(node=head2))
