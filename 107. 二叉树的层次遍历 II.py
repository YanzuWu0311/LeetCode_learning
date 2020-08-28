"""
二叉树遍历
深度优先，分别递归到左右子树里面去
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arr = []

        def inner(node, level):
            if node is not None:
                if len(arr) < level + 1:
                    arr.append([])  # 加一[]
                arr[level].append(node.val)
                inner(node.left, level + 1)
                inner(node.right, level + 1)

        inner(root, 0)
        arr.reverse()
        return arr


floor2_1 = TreeNode(15)
floor2_2 = TreeNode(7)
floor1_1 = TreeNode(9)
floor1_2 = TreeNode(20)
floor1_2.left = floor2_1
floor1_2.right = floor2_2
root = TreeNode(3)
root.left = floor1_1
root.right = floor1_2

Solution_levelOrderBottom = Solution()
result = Solution_levelOrderBottom.levelOrderBottom(root)
print(result)
