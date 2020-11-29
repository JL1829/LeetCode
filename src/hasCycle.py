"""
给定一个链表， 判断其是否回环
若有环， 返回True
没有环， 返回False

# Solution
显而易见，可以使用快慢指针法
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node with value: {self.value}"


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

node5 = ListNode(1)
node5.next = ListNode(2)
node5.next.next = ListNode(3)


def hasCycle(node):
    if not node or not node.next:
        return False

    slow = node
    fast = node.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


if __name__ == '__main__':
    print(f"For Linked List started with {node1}, have loop? \n {hasCycle(node=node1)}\n")
    print(f"For Linked List started with {node5}, have loop? \n {hasCycle(node=node5)}\n")
