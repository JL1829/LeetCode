class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f"Linked List Node: {self.value}"

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

def LinkListTraversal(head):
    if head.next is None:
        return head
    while head:
        print(head.value)
        head = head.next

LinkListTraversal(head)

def deleteNode(head, value):
    if head.value == value:
        return head.next
    pre, current = head, head.next
    while current and current.value != value:
        pre, current = current, current.next
    if current:
        pre.next = current.next
    
    return head

print(f"Now delete node with value 5")
head = deleteNode(head, 5)
LinkListTraversal(head)