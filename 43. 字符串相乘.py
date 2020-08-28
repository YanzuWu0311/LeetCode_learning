"""
把字符串转化为数字，相乘的结果转化为字符串
其他，利用了python得天独厚的int无限长的特性，直接用python的int(),str()进行转换
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 * num2)


num1 = '123'
num2 = '456'
Solution_multiply = Solution()
print(Solution_multiply.multiply(num1, num2))
