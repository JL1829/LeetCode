"""
实现一种算法，找出单向链表中的倒数第`k` 个节点。返回该节点的值

链表1： 1 -> 2 -> 3 -> 4 -> 5
k = 2
返回：4

# Solution
使用快慢指针法。

题目求倒数第`k`个节点的值，先让快指针跑到`k` 位置， 若还没有到`None`
则固定快慢指针的距离，快慢指针一同往前走，若快指针到`None`了
则慢指针就是倒数`k`位置， 输出其值即可。
"""


class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node with value: {self.value}"


def printLinkedList(node):
    value = []
    while node:
        value.append(node.value)
        node = node.next
    return value


def kthToLast(node, k):
    fast = node
    slow = node

    while k > 0:
        fast = fast.next
        k -= 1
    while fast is not None:
        fast = fast.next
        slow = slow.next

    return slow.value


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # expected: [1, 2, 3, 4, 5]
    print(printLinkedList(node=head))

    # expected: 4
    print(kthToLast(node=head, k=2))
