"""
判断一个字符串里面有几个回文子串
动态规划，遍历顺序很重要，若按传统的上三角形逐行遍历，那么一开始的那一行是最长的，显然不合适，要按下三角形逐行遍历
"""


class Solution:
    def countSubstrings(self, s):
        # dp[i][j] 代表 子串[i, j] 是否是一个 回文串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        # 枚举所有可能 因为代表子串 所以 i <= j
        # 遍历顺序很重要，若按传统的上三角形逐行遍历，那么一开始的那一行是最长的，显然不合适，要按下三角形逐行遍历
        for j in range(n):
            for i in range(0, j + 1):
                # 子串长度
                length = j - i + 1
                # 只有一个字符 直接就是一个回文串
                if length == 1:
                    dp[i][j] = True
                    count += 1
                # 两个字符 只有相等才是回文串
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                # 超过两个字符 首位相同 且除去首尾的子串是回文串 才是回文串
                if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    count += 1
        return count


s = 'aaa'
Solution_countSubstrings = Solution()
print(Solution_countSubstrings.countSubstrings(s))
