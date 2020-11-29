# Author: Johnny Lu
# Time: 27th/Nov/2020
# Contacts: joh@johdev.com
"""
Linked List
"""


class ListNode:
    """
    The basic node in Linked List
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node with value: {self.value}"


class LinkedList:
    """
    This is single linked list, have below method:

    To be continue
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.head = ListNode()
        self.TailNode = None
        self.length = 0

    def __len__(self):
        return self.length

    def __repr__(self):
        return f"Single Linked List with length: {self.length}\n" \
               f"And with full element: {self._printValue()}"

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Linked List is FULL!")

        node = ListNode(value)
        TailNode = self.TailNode
        if TailNode is None:
            self.head.next = node
        else:
            TailNode.next = node
        self.TailNode = node
        self.length += 1

    def appendLeft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Linked List is FULL!")
        node = ListNode(value)
        # if original linked list is empty, insert first element need to set TailNode
        if self.TailNode is None:
            self.TailNode = node

        headNode = self.head.next
        self.head.next = node
        node.next = headNode

        self.length += 1

    def __iter__(self):
        for node in self._iter_node():
            yield node.value

    def _iter_node(self):
        """
        Traversal from head to tail
        """
        currentNode = self.head.next
        while currentNode is not self.TailNode:
            yield currentNode
            currentNode = currentNode.next
        if currentNode is not None:
            yield currentNode

    def _printValue(self):
        value = []
        node = self.head.next
        while node:
            value.append(node.value)
            node = node.next

        return value


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    print(ll)
