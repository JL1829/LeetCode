class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Tree Node value: {self.value}"


root = TreeNode(5)
root.right = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)


def kthSmallest_recursive(node, k):
    def inorder(node):
        if not node:
            return []

        return inorder(node.left) + [node.value] + inorder(node.right)

    return inorder(node)[k - 1]


print(kthSmallest_recursive(root, 3))


def kthSmallest_iterate(node, k):
    stack = []

    while True:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if not k:
            return node.value
        node = node.right


print(kthSmallest_iterate(root, 3))
