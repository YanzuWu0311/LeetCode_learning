"""
是否回文数字
创建一个新的字符串数组，把原数组从最后一个字符开始，放入新的数组
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_num = str(x)
        new_str = ''
        for i in range(len(str_num) - 1, -1, -1):
            new_str += str_num[i]

        return new_str == str_num


x = -121
Solution_isPalindrome = Solution()
print(Solution_isPalindrome.isPalindrome(x))
