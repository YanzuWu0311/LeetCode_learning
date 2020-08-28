"""
判断一些括号的组合是否合法
栈的性质，遍历字符串，左括号压栈，右括号判断与栈顶的括号是否对应，对应即把栈顶的左括号pop，不对应或者栈是空的，就错了，结果看栈是不是空的
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:  # 如果字符串的长度为奇数，直接错误
            return False
        pairs_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []  # 用堆栈存储括号
        # 对于左括号
        # 我们对给定的字符串 s 进行遍历，当我们遇到一个左括号时，我们会期望在后续的遍历中，有一个相同类型的右括号将其闭合。由于后遇到的左括号要先闭合，因此我们可以将这个左括号放入栈顶
        # 对于右括号
        # 当我们遇到一个右括号时，我们需要将一个相同类型的左括号闭合。此时，我们可以取出栈顶的左括号并判断它们是否是相同类型的括号。如果不是相同的类型，或者栈中并没有左括号，那么字符串 s 无效，返回False。
        # 为了快速判断括号的类型，我们可以使用哈希映射（HashMap）存储每一种括号。哈希映射的键为右括号，值为相同类型的左括号
        # 在遍历结束后，如果栈中没有左括号，说明我们将字符串 s 中的所有左括号闭合，返回 True，否则返回 \text{False}False。
        for ch in s:
            if ch in pairs_dict:  # 若为右括号
                if not stack or stack[-1] != pairs_dict[ch]:  # 若此时stack已经空了，或者栈顶的不是对应的左括号
                    return False
                stack.pop()  # 否则把栈顶的元素pop出来
            else:  # 遇到左括号就直接添加在栈顶
                stack.append(ch)
        return not stack  # 若结束遍历后stack还有东西，就False


s = '([)]'
Solution_isValid = Solution()
print(Solution_isValid.isValid(s))
