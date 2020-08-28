"""
zigzag模式重写字符串
遍历原字符串，将不同的字符放进不同的行中即可
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):  # 当原字符串不足以折一次上去
            return s
        res = [''] * numRows  # 设置placeholder 相当于分成numRows行，以便后面把不同的字符插入
        row, step = 0, 0
        for temp in s:  # 遍历原字符串中的每一个字符
            res[row] += temp
            if row == 0:  # 到顶后，开始往下走，行的index加一
                step = 1
            if row == numRows - 1:  # 到底后，开始往上走，行的index减一
                step = -1
            row += step
        return ''.join(res)


str = 'PAYPALISHIRING'
num = 4
Solution_convert = Solution()
print(Solution_convert.convert(str, num))
