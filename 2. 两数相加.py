"""
两个链表的数当作整数相加，结果放在另一个链表中
构建链表类
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def Creat_list(self, num):
        n = len(num)
        if n <= 0:
            return False
        if n == 1:
            return ListNode(val=num[0], next=None)  # 只有一个节点
        else:
            root = ListNode(val=num[0], next=None)
            tmp = root
            for i in range(2, n + 1):  # 一个一个的增加节点
                tmp.next = ListNode(val=num[i - 1], next=None)
                tmp = tmp.next
        return root  # 返回根节点

    def print_list(self, head):  # 打印链表 （遍历）
        p = head
        print(str(p.val), end='')
        p = p.next
        while p is not None:
            print("——>" + str(p.val), end='')
            p = p.next

    def list_len(self, head):  # 链表长度
        count = 0
        p = head
        while p is not None:
            count = count + 1
            p = p.next
        return count


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp1_list = []
        while temp1 is not None:
            temp1_list.append(temp1.val)
            temp1 = temp1.next
        Wei_shu1 = len(temp1_list)
        digit1 = 0
        for i in range(Wei_shu1):
            digit1 = digit1 + temp1_list[i] * 10 ** i
        temp2 = l2
        temp2_list = []
        while temp2 is not None:
            temp2_list.append(temp2.val)
            temp2 = temp2.next
        Wei_shu2 = len(temp2_list)
        digit2 = 0
        for i in range(Wei_shu2):
            digit2 = digit2 + temp2_list[i] * 10 ** i

        ans = digit1 + digit2
        ans_list = [int(char) for char in str(ans)]
        ans_list.reverse()
        l3 = ListNode()
        l3_root = l3.Creat_list(ans_list)
        return l3_root


numbers = [2, 4, 3]
Head_node1 = ListNode()
root1 = Head_node1.Creat_list(numbers)
Head_node1.print_list(root1)
print('')
numbers = [5, 6, 4]
Head_node2 = ListNode()
root2 = Head_node2.Creat_list(numbers)
Head_node2.print_list(root2)

print('')

Solution_addtwonumbers = Solution()
result = Solution_addtwonumbers.addTwoNumbers(root1, root2)
result_root = result
result.print_list(result_root)
