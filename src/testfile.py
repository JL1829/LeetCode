# 典型数组遍历框架
array = [1, 2, 3, 4, 5]


def traverse(array):
    for item in array:
        print(item)

# traverse(array)


# 典型链表遍历
class TreeNode:
    """DocString placeholder"""

    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Tree Node value: {self.value}"


head = TreeNode(1)
head.next = TreeNode(2)
head.next.next = TreeNode(3)


# 迭代访问
def LinkedListTraverse(head):
    p = head
    while p is not None:
        print(p.value)
        p = p.next

# LinkedListTraverse(head)


# 递归访问
def recursiveLinkedList(head):
    print(head.value)
    if head is not None:
        recursiveLinkedList(head.next)


recursiveLinkedList(head)
