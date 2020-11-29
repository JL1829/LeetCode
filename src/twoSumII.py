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
root.right.right.left = TreeNode(5)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)


# DFS method

def pathSum(node, total):
    ret = []
    path = []

    def dfs(node, total):
        if not node:
            return
        path.append(node.value)
        total -= node.value
        if not node.left and not node.right and total == 0:
            ret.append(path[:])
        dfs(node.left, total)
        dfs(node.right, total)
        path.pop()

    dfs(node=node, total=total)
    return ret


print(pathSum(root, 22))
