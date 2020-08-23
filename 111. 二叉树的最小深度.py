# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 建立二叉树是以层序遍历方式输入，节点不存在时以 'None' 表示
    def creatTree(self, nodeList):
        if nodeList is None:  # 若nodeList为空
            return None
        head = TreeNode(nodeList[0])  # 创建根节点
        Nodes = [head]
        j = 1
        for node in Nodes:
            if node is not None:
                node.left = (TreeNode(nodeList[j]) if nodeList[j] is not None else None)  # 先创建左子树
                Nodes.append(node.left)
                j += 1
                if j == len(nodeList):  # 用完所有节点
                    return head
                node.right = (TreeNode(nodeList[j]) if nodeList[j] is not None else None)  # 再创建右子树
                j += 1
                Nodes.append(node.right)
                if j == len(nodeList):
                    return head

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:  # 当节点为空时
            return 0
        elif root.right is None and root.left is None:  # 当为叶节点时
            return 1
        elif root.right is None and root.left is not None:  # 当只有一个子树时
            return self.minDepth(root.left) + 1
        elif root.right is not None and root.left is None:  # 当只有一个子树时
            return self.minDepth(root.right) + 1
        elif root.right is not None and root.left is not None:  # 有两个子树时
            left_minDepth = self.minDepth(root.left)
            right_minDepth = self.minDepth(root.right)
            return min(left_minDepth, right_minDepth) + 1


nodelist = [1, 2, None, 3, None, 4, None, 5]
Solution_minDepth = Solution()
root = Solution_minDepth.creatTree(nodelist)
print(Solution_minDepth.minDepth(root))
