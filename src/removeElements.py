"""
删除链表中给定值`val`的所有节点

**示例**
链表： `1 -> 2 -> 3 -> 4 -> 5 -> 6`
val = `6`
输出： `1 -> 2 -> 3 -> 4 -> 5`

链表： `1 -> 2 -> 3 -> 4 -> 5 -> 6`
val = 3
输出： `1 -> 2 -> 4 -> 5 -> 6`

# Solution
创建哨兵伪头节点，以方便操作

"""
from utilis.linkedList import ListNode


def printLinkedList(node):
    value = []
    while node:
        value.append(node.value)
        node = node.next

    return value


def removeElement(node: ListNode, val: int) -> ListNode:
    sentinel = ListNode(None)
    sentinel.next = node

    previous = sentinel
    current = node

    while current:
        if current.value == val:
            previous.next = current.next
        else:
            previous = current
        current = current.next

    return sentinel.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    print(printLinkedList(node=node1))
    print(removeElement(node=node1, val=3))
    print(printLinkedList(node=node1))
