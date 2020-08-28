"""
找最长的回文子串
动态规划
"""
import numpy as np


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ''
        result_len = 0

        dp = [[0] * len(s) for _ in range(len(s))]
        # 构建len(s)*len(s)的矩阵
        # 若为1，则表示是回文
        for i in range(len(s)):  # 初始化
            for j in range(len(s)):
                if i == j:
                    dp[i][j] = 1
                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = 1

        for j in range(0, len(s)):  # 非常规的循环
            for i in range(len(s)):
                if j == 0:
                    dp[i][i + j] = 1
                elif j == 1:
                    if i + j <= len(s) - 1:
                        if s[i] == s[i + j]:
                            dp[i][j] = 1
                elif i + j <= len(s) - 1:
                    if s[i] == s[i + j] and dp[i + 1][i + j - 1] == 1:
                        dp[i][i + j] = 1

        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == 1:
                    if j - i + 1 > result_len:  # 存储长度最大的回文子串
                        result = s[i:j + 1]
                        result_len = j - i + 1
        # print(np.array(dp))
        return result


s = 'cbbd'
Solution_longestPalindrome = Solution()
print(Solution_longestPalindrome.longestPalindrome(s))
