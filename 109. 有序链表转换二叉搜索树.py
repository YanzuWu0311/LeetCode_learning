"""
把一个升序的链表转换为平衡二叉树
分治，先找链表的中间值，把他作为根节点，链表的头到中间值这一段中再找一个中间值，作为根的左子树，从中间值到链表的尾，找一个中间值，作为根的右子树
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def getMedian(left, right):  # left表示链表的头，right表示链表的尾
            fast = slow = left  # fast每次移动两次， slow每次移动一次
            while fast != right and fast.next != right:  # fast移动到头后，slow指向中间数
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left, right):
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)  # 先把中间值作为根
            root.left = buildTree(left, mid)  # 根的左子树就是left到mid的中间数
            root.right = buildTree(mid.next, right)  # 根的右子树就是mid的下一个到right的中间数
            return root

        return buildTree(head, None)


node_list = [-10, -3, 0, 5, 9]
head = ListNode(-10)
follow1 = ListNode(-3)
follow2 = ListNode(0)
follow3 = ListNode(5)
follow4 = ListNode(9)
head.next = follow1
follow1.next = follow2
follow2.next = follow3
follow3.next = follow4
Solution_sortedListToBST = Solution()
print(Solution_sortedListToBST.sortedListToBST(head))
