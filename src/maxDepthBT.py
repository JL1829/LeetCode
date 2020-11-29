"""
给定一个二叉树，找出其最大深度
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数

**说明**
叶子节点指的是没有子节点的节点

**示例**

给定二叉树：[3, 9, 20, Null, null, 15, 7]
    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度为：`3`

# Solution
## 层次遍历

"""
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Tree Node with Value: {self.value}"


def maxDepth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append([1, root])
    while queue:
        depth, node = queue.popleft()
        if node.left:
            queue.append((depth + 1, node.left))
        if node.right:
            queue.append((depth + 1, node.right))

    return depth


if __name__ == '__main__':
    Treenode = TreeNode(3)
    Treenode.left = TreeNode(9)
    Treenode.right = TreeNode(20)
    Treenode.right.left = TreeNode(15)
    Treenode.right.right = TreeNode(7)
    print(f"The max depth of this Binary Tree is: \n {maxDepth(root=Treenode)}")
