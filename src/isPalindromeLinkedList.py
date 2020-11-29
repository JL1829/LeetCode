"""
请判断一个链表是否为回文链表

**示例**
输入： 1 -> 2
输出: False

输入: 1 -> 2 -> 2 -> 1
输出: True

**test case**

# Solution

"""


class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"List Node Value: {self.value}"


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

head1 = ListNode(1)
head1.next = ListNode(2)


def convertToList(node):
    value = []
    while node:
        value.append(node.value)
        node = node.next

    return value


if __name__ == '__main__':
    array = convertToList(node=head)
    array2 = convertToList(node=head1)
    print(array == array[::-1])
    print(array2 == array2[::-1])
