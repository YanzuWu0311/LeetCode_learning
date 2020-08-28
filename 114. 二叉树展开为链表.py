"""
把二叉树转换成只有右子树的树

若节点的左子树存在
    先保存右子树
    把右子树替换为左子树
    删除左子树
    最后把原先的右子树接在最右下
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 由题图易知，将二叉树化为链表就是把二叉树变为只有右子树的二叉树。而按照这样的思路
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            # 若根节点的左子树存在
            tmp = root.right
            # 先保存你右子树
            root.right = root.left
            # 用左子树替换右子树
            root.left = None
            # 把左子树清除
            node = root.right
            while node.right:
                node = node.right
            node.right = tmp
            # 把原先的右子树接在最右下


root = TreeNode(1)
floor1_1 = TreeNode(2)
floor1_2 = TreeNode(5)
floor2_1 = TreeNode(3)
floor2_2 = TreeNode(4)
floor2_3 = TreeNode(6)
root.left = floor1_1
root.right = floor1_2
floor1_1.left = floor2_1
floor1_1.right = floor2_2
floor1_2.right = floor2_3
Solution_flatten = Solution()
Solution_flatten.flatten(root)

temp = root
result_list = []
while temp is not None:
    result_list.append(temp.val)
    temp = temp.right
print(result_list)
