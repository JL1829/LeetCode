class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Tree Node with value: {self.value}"


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


# 以下都是递归方式遍历
def preOrder(root):
    if not root:
        return []
    
    return [root.value] + preOrder(root.left) + preOrder(root.right)


print(f"Pre Order of a Tree called root: {preOrder(root)}")


def inorder(root):
    if not root:
        return []
    
    return inorder(root.left) + [root.value] + inorder(root.right)


print(f"In Order traversal of a tree call root: {inorder(root)}")


def postOrder(root):
    if not root:
        return []
    return postOrder(root.left) + postOrder(root.right) + [root.value]


print(f"Post Order Traversal of a tree call root: {postOrder(root)}")


# 迭代方式遍历
def iteratePreOrder(root):
    if not root: return []

    result = []
    stack = [root]
    while stack:
        cur = stack.pop()
        result.append(cur.value)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    
    return result


print(f"Iterate throught: {iteratePreOrder(root)}")

# flip binary tree

