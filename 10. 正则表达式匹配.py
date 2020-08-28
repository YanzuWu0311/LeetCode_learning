"""
手写与正则表达式相同的函数去匹配
动态规划，或者直接用re模块
"""
import re
import numpy as np


class Solution1(object):
    def isMatch(self, s, p):
        # 题目设计的和python里re模块正则表达式一样
        return re.match('^' + p + '$', s) is not None
        # '^'表示匹配字符串开头
        # '$'表示匹配字符串结尾


class Solution(object):
    def isMatch(self, text, pattern):
        # 建立dp[m+1][n+1]数组
        # 横排m+1代表空白一个首元素+s中的m个元素，竖排n+1代表空白一个元素+p中的n个元素
        m = len(text)
        n = len(pattern)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1  # 表示空的，当text和pattern都是空的时候，当然True
        # 竖的表示text， 横的表示pattern
        # 初始化第0列,除了[0][0]全为false，毋庸置疑，因为空串p只能匹配空串，其他都无能匹配
        for i in range(1, m + 1):
            dp[i][0] = 0
        # 初始化第0行，只有X*能匹配空串，如果有*，它的真值一定和p[0][j-2]的相同（略过它之前的符号）
        for i in range(2, n + 1):
            # 要匹配一个空串，只有当前是‘*’并且上一个匹配成功
            if pattern[i - 1] == '*' and dp[0][i - 2]:
                dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 这里j-1才是正常字符串中的字符位置
                # 若当第j个字符是‘*’时，返回True的情况
                # 1.若第j-1个pattern匹配失败，需要dp[i][j-2]为True，那么‘*’把pattern第j-1个字符出现0次，则匹配成功
                # 2.若第j-1个pattern匹配成功(相等或为‘.’)，还需要保证当前pattern和除去最后一个字符的text匹配成功
                if pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j]
                else:
                    dp[i][j] = ((pattern[j - 1] == '.' or text[i - 1] == pattern[j - 1]) and dp[i - 1][j - 1])

        print(np.array(dp))
        if dp[m][n] == 1:
            return True
        else:
            return False


s = 'aab'
p = 'c*a*b'
Solution_isMatch = Solution()
print(Solution_isMatch.isMatch(s, p))
