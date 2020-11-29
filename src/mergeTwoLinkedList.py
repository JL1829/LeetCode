"""
将两个升序链表合并为一个新的升序链表并返回
新链表是通过拼接给定的两个链表的所有节点组成的。

**示例**
输入： 1->2->4, 1->3->4
输出： 1->1->2->3->4->4

**test case**
>>> head1 = ListNode(1)
>>> head1.next = ListNode(2)
>>> head1.next.next = ListNode(4)
>>> head2 = ListNode(1)
>>> head2.next = ListNode(3)
>>> head2.next.next = ListNode(4)

>>> mergeTwoLinkedList(l1=head1, l2=head2)
1
1
2
3
4
4
None
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Linked List Node with value: {self.value}"


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)


def printLinkedList(head):
    while head:
        print(head.value)
        head = head.next


# print(f"{printLinkedList(head1)}")


def mergeTwoLinkedList(l1, l2):
    prehead = ListNode(-1)
    prev = prehead

    while l1 and l2:
        if l1.value <= l2.value:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next

    prev.next = l1 if l1 is not None else l2

    return prehead.next


mergeTwoLinkedList(l1=head1, l2=head2)
print(f"{printLinkedList(head1)}")
