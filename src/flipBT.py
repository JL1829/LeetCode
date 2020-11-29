class TreeNode:
    """DocString Placeholder"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Tree Node value: {self.value}"


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


def preOrder(node):
    if not node:
        return []
    return [node.value] + preOrder(node.left) + preOrder(node.right)


print(f"Pre Order: {preOrder(root)}")


def invertTree(node):
    if not node:
        return
    node.left, node.right = invertTree(node.right), invertTree(node.left)
    return node


print(f"Inverting Tree")
invertTree(node=root)
print(f"Pre Order after invert: {preOrder(root)}")
