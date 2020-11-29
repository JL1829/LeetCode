"""
# 设计链表（单链表）

设计链表的实现，选择单链表或者双向链表，节点中都应该具有两个属性：`val` 和`next`, `val`是
当前节点的值，`next` 是指向下一个节点的指针/引用.

假设链表是0-index.

构造一个链表类，实现以下功能：

* get(index): return value of List Node at index
* addAtHead(val): add node at the head
* addAtTail(val): add node at the tail
* addAtIndex(index, val): add node at the index
* deleteAtIndex(index): delete the node at index

**Example**

>>> linkedList = MyLinkedList()
>>> linkedList.addAtHead(1)
>>> linkedList.addAtHead(3)
>>> linkedList.addAtIndex(1, 2)

# now linkedlist become: 1 -> 2 -> 3

>>> linkedList.get(1)

# return 2

>>> linkedList.deleteAtIndex(1)

now linkedlist become: 1 -> 3

>>> linkedList.get(1)

now return 3
"""


class ListNode:
    """docString"""

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"List Node with value: {self.val}"


class MyLinkedList:
    """docString"""

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0
        self.tailNode = None

    def __len__(self):
        return self.length

    def __iter__(self):
        # for node in self.iter_node():
        #     yield node.val
        pass

    def iter_node(self):
        pass

    def __repr__(self):
        return f"Linked List Object with length: {self.length}"

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked List.
        If the index is invalid, return -1
        """
        if index < 0 or index > self.length:
            return -1
        node = self.head
        for _ in range(index + 1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add the Value at the head of the link list
        """
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new

        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Add the value at the end of the link list
        """
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(val)

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value `val` before the index-th node in the linked
        List, if index equals to the length of linked list, the node
        will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted
        """
        if index > self.length:
            return

        if index < 0:
            index = 0

        node = self.head
        for i in range(index):
            if node is None:
                return
            node = node.next
        if node is None:
            node = ListNode(val)
        else:
            new = ListNode(val)
            new.next = node.next
            node.next = new

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid
        """
        if index < 0 or index > self.length:
            return

        node = self.head
        for _ in range(index):
            node = node.next
        if node.next is not None:
            node.next = node.next.next

        self.length = -1

    def printValue(self) -> list:
        value = []
        while self.head:
            value.append(self.head.val)
            self.head = self.head.next

        return value
