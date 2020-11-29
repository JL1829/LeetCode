"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。
传入函数的**唯一参数** 是 **要被删除的节点**

现在有一链表：
[4, 5, 1, 9]
它表示为：4 -> 5 -> 1 -> 9
删除节点5， 返回：[4, 1, 9], 因为： 5 被移除了，链表表示为： 4 -> 1 -> 9
**注意**
你只知道要被删除的节点，它的上一个节点你不知道。

**test case**
>>> head = ListNode(4)
>>> head.next = ListNode(5)
>>> head.next.next = ListNode(1)
>>> head.next.next.next = ListNode(9)
>>> print(printLinkedList(node=head))
[4, 5, 1, 9]

>>> deleteNode(node=head)
>>> print(printLinkedList(node=head))
[4, 1, 9]

"""


class ListNode:
    """docString Placeholder"""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node with value: {self.value}"

    __str__ = __repr__


def deleteNode(node):
    node.value = node.next.value
    node.next = node.next.next


def printLinkedList(node):
    value = []
    if not node:
        return []
    while node:
        value.append(node.value)
        node = node.next

    return value


if __name__ == '__main__':
    head1 = ListNode(4)
    head1.next = ListNode(5)
    head1.next.next = ListNode(1)
    head1.next.next.next = ListNode(9)
    LinkedList = printLinkedList(node=head1)
    print(LinkedList)
