"""
给定一个链表，删除链表的倒数第`n`个节点，并且返回链表的头节点

**示例**

链表: 1 -> 2 -> 3 -> 4 -> 5
n = 2
当删除了倒数第二个节点：`4`之后，链表变成： 1 -> 2 -> 3 -> 5

**说明**
给定的`n`保证是有效的

**进阶**
你能用一趟扫描完成吗？
即是：
时间复杂度： $O(n)$
空间复杂度： $O(1)$

# Solution
快慢指针
我们也可以在不预处理出链表的长度，以及使用常数空间的前提下解决本题。
由于我们需要找到倒数第 n 个节点，因此我们可以使用两个指针 fast 和 slow 同时遍历
并且fast 比slow 超前 n 个节点，当fast 遍历到链表末尾的时候，slow 就恰巧在倒数第`n`个节点处。

具体的， 初始时fast 和slow 均指向头结点，我们首先使用fast对链表进行遍历，遍历的次数为`n`
此时，fast 和 slow之间间隔了`n - 1`个节点，即fast 比slow 快了 `n`个节点。

到这个时候，我们同时使用fast和slow同步进行遍历，当fast遍历到链表末尾（即fast is None)的时候，slow 恰好指向
倒数第`n`个节点。

我们可以考虑在初始化的时候将slow 指向 dummy 节点，其余步骤不便，这样一来，当fast遍历到链表末尾时，slow的下一个
节点即是我们要删除的节点
使用
slow.next = slow.next.next 去删除。
"""


class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"List Node with Value: {self.value}"


def printLinkedList(node):
    value = []
    while node:
        value.append(node.value)
        node = node.next

    return value


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(f"The original linked list: {printLinkedList(node=head)}")


def removeNthFromEnd(node, n):
    dummy = ListNode(0, node)
    fast = node
    slow = dummy
    for _ in range(n):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


head = removeNthFromEnd(node=head, n=2)
print(f"After removal: {printLinkedList(node=head)}")
