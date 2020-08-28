"""
每个节点有权重，选中的节点不能直接相连，求最大值
动态规划，从root开始，left[0]表示该节点抢的最大值, left[1]表示该节点不抢的最大值，right相同，每个节点由其两个子节点算出
# 我们可以用 f(o) 表示选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和；
# g(o) 表示不选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和
# l 和 r 代表 o 的左右孩子。

# 当 o 被选中时，o 的左右孩子都不能被选中，故 o 被选中情况下子树上被选中点的最大权值和为 l 和 r 不被选中的最大权值和相加，即 f(o) = g(l) + g(r) + o。
# 当 o 不被选中时，o 的左右孩子可以被选中，也可以不被选中。对于 o 的某个具体的孩子 x，它对 o 的贡献是 x 被选中和不被选中情况下权值和的较大值。故 g(o) = max{f(l),g(l)}+max{f(r),g(r)}

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.dfs(root)
        return max(result[0], result[1])

    def dfs(self, root):
        if root is None:
            return 0, 0
        else:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            robValue = left[1] + right[1] + root.val
            # 若要抢，那两个子节点不能抢
            skipValue = max(left[0], left[1]) + max(right[0], right[1])
            # 若不抢，则两个子节点随便，可以抢，可以不抢
            # left[0], right[0]表示抢
            # left[1], right[1]表示不抢
            return robValue, skipValue


root = TreeNode(3)
floor1_1 = TreeNode(2)
floor1_2 = TreeNode(3)
floor2_1 = TreeNode(3)
floor2_2 = TreeNode(1)
root.left = floor1_1
root.right = floor1_2
floor1_1.right = floor2_1
floor1_2.right = floor2_2
Solution_rob = Solution()
print(Solution_rob.rob(root))
