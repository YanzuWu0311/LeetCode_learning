"""
判断一棵树是不是平衡二叉树，一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1
深度优先，从root开始，不断找每个点是不是合格，即返回其左右两个节点的深度，进行比较，用一个flag表示是否合法
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.flag = True

    def Tree_depth(self, root):
        if root is None:
            return 0
        leftDepth = self.Tree_depth(root.left)
        rightDepth = self.Tree_depth(root.right)
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node):
            if node is None or self.flag is False:
                return
            if node.left is not None:
                left_depth = self.Tree_depth(node.left)
            else:
                left_depth = 0
            if node.right is not None:
                right_depth = self.Tree_depth(node.right)
            else:
                right_depth = 0
            if abs(left_depth - right_depth) > 1:
                self.flag = False
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.flag


floor1 = TreeNode(1)
floor2_1 = TreeNode(2)
floor2_2 = TreeNode(2)
floor3_1 = TreeNode(3)
floor3_2 = TreeNode(3)
floor4_1 = TreeNode(4)
floor4_2 = TreeNode(4)
floor1.left = floor2_1
floor1.right = floor2_2
floor2_1.left = floor3_1
floor2_1.right = floor3_2
floor3_1.left = floor4_1
floor3_1.right = floor4_2
Solution_isBalanced = Solution()
print(Solution_isBalanced.isBalanced(floor1))
