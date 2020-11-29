"""
翻转一个单向链表

链表： 1 -> 2 -> 3 -> 4 -> NULL
翻转： 4 -> 3 -> 2 -> 1 -> NULL

**进阶**
使用迭代或者递归翻转链表，你能否用两种方法解决问题？

解答
![solution](https://pic.leetcode-cn.com/039a6eff23111dba77d91ed909bbd35539b1185c07664372b129216a7b779b4a-image-20200627220535158.png)
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node value: {self.value}"


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


def printLinkList(node):
    value = []
    while node:
        value.append(node.value)
        node = node.next

    return value


print(f"Original Linked List: {printLinkList(node=head)}")


def reverseLinkList(node):
    pre = None
    current = node
    while current:
        temp = current.next
        current.next = pre
        pre = current
        current = temp
    return pre


head = reverseLinkList(node=head)
print(f"After Reverse: {printLinkList(node=head)}")
