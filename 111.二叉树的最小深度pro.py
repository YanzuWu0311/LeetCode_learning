# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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

    def minDepth_shendu(self, root):
        if not root:  # 该节点为空
            return 0

        if not root.left and not root.right:  # 为叶节点
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth_shendu(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth_shendu(root.right), min_depth)

        return min_depth + 1

    def minDepth_guangdu(self, root):  # 广度优先
        if not root:  # 若为空节点，返回0
            return 0

        que = collections.deque([(root, 1)])  # deque是双边队列
        # 初始值里面只有一个元组 root表示根节点，1表示最小深度
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:  # 该节点已经没有子树了，直接返回此时的深度
                return depth
            if node.left:  # 若有左子树
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return 0


nodelist = [1, 2, None, 3, None, 4, None, 5]
Solution_minDepth = Solution()
root = Solution_minDepth.creatTree(nodelist)
print(Solution_minDepth.minDepth_shendu(root))
