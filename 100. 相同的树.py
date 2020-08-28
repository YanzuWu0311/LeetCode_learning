"""
检测两棵树是否相同
深度优先，首先，若两个节点不是None，需要其val相同，左右子树相同才会相同；若两个节点都是None，则相同；其余情况均不同
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is not None and q is not None:
            if p.val == q.val:
                left_situation = self.isSameTree(p.left, q.left)
                right_situation = self.isSameTree(p.right, q.right)
                return left_situation and right_situation
            else:
                return False
        elif p is None and q is None:
            return True
        else:
            return False
