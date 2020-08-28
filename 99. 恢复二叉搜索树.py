"""
把二叉搜素树重新排成正确的顺序（交换错误的两个节点的值）
其他，中序遍历二叉树，若为正确的二叉搜索树，那么为增序。找出其中错误的index，再在树中找出对应的节点，交换其val
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 我们来看下如果在一个递增的序列中交换两个值会造成什么影响。假设有一个递增序列 a=[1,2,3,4,5,6,7]。如果我们交换两个不相邻的数字，例如 2 和 6，原序列变成了
# a=[1,6,3,4,5,2,7]，那么显然序列中有两个位置不满足 ai<a{i+1}，在这个序列中体现为
# 6>3，5>2，因此只要我们找到这两个位置，即可找到被错误交换的两个节点。
# 如果我们交换两个相邻的数字，例如 2 和 3，此时交换后的序列只有一个位置不满足 ai<a{i+1} ​
# 因此整个值序列中不满足条件的位置或者有两个，或者有一个。


# 它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
# 1.找到二叉搜索树 中序遍历 得到值的序列的不满足条件的位置
# 2.若有两个位置，记为i，j(i<j)，即 ai>a{i+1}&&aj>a{j+1}，那么对应被错误交换的节点即为 ai对应的节点和 a{j+1}对应的节点，我们分别记为 x 和 y
# 3.如果有一个，我们记为 i，那么对应被错误交换的节点即为 ai对应的节点和 a{i+1}对应的节点，我们分别记为 x 和 y
# 4.交换x，y


class Solution(object):
    def __init__(self):  # 整个类都要用到
        self.middle_digui_list = []  # 中序遍历的结果
        self.error_list = []  # 排序错误的index

    def PrintFromTopToBottom(self, root):  # 层次遍历
        # write code here
        outList = []
        queue = [root]
        while queue != [] and root:
            outList.append(queue[0].val)
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.pop(0)
        return outList

    def middle_digui(self, root):  # 中序遍历
        if root is None:
            return
        self.middle_digui(root.left)
        self.middle_digui_list.append(root.val)
        self.middle_digui(root.right)

    def Find_node(self, root, value):  # 从二叉树中找对应的节点
        if root is not None:
            if root.val == value:
                return root
            else:
                left_result = self.Find_node(root.left, value)
                if left_result is not None:
                    return left_result
                else:
                    return self.Find_node(root.right, value)
        else:
            return

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.middle_digui(root)
        for i in range(len(self.middle_digui_list) - 1):  # 查看不按顺序排的index
            if self.middle_digui_list[i] > self.middle_digui_list[i + 1]:
                self.error_list.append(i)
        if len(self.error_list) == 1:
            front_node = self.Find_node(root, self.middle_digui_list[self.error_list[0]])
            back_node = self.Find_node(root, self.middle_digui_list[self.error_list[0] + 1])
            temp = front_node.val
            front_node.val = back_node.val
            back_node.val = temp
        elif len(self.error_list) == 2:
            front_node = self.Find_node(root, self.middle_digui_list[self.error_list[0]])
            back_node = self.Find_node(root, self.middle_digui_list[self.error_list[1] + 1])
            temp = front_node.val
            front_node.val = back_node.val
            back_node.val = temp
        return self.PrintFromTopToBottom(root)


root = TreeNode(3)
floor1_1 = TreeNode(1)
floor1_2 = TreeNode(4)
floor2 = TreeNode(2)
root.left = floor1_1
root.right = floor1_2
floor1_2.left = floor2
Solution_recoverTree = Solution()
print(Solution_recoverTree.PrintFromTopToBottom(root))
print(Solution_recoverTree.recoverTree(root))
