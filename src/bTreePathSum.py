from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Tree Node: {self.value}"


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)


def preOrder(node):
    if not node:
        return None
    print(node.value)
    preOrder(node.left)
    preOrder(node.right)


# preOrder(root)
"""
def accumulate(node):
    if not node:
        return False
    queue.append((node, node.value))
    accumulate(node.left)
    accumulate(node.right)
"""


# queue = deque()
# accumulate(root)
# print(queue)

def hasPathSum(node, total):
    if not node:
        return False
    queue = deque()
    queue.append((node, node.value))
    while queue:
        node, path = queue.popleft()
        if not node.left and not node.right and path == total:
            return True
        if node.left:
            queue.append((node.left, path + node.left.value))
        if node.right:
            queue.append((node.right, path + node.right.value))
    return False


print(hasPathSum(root, 22))
