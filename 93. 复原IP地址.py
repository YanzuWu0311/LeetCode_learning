"""
把一串数字内容的字符串分成4段，每段数字大小0~255，找出所有可能
深度优先，找出所有有可能的结果，遇到有问题的就直接return不浪费时间
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seg_count = 4  # 分成4段
        result = []
        segments = [0] * seg_count

        def dfs(segid, segstart):
            #  表示我们正在从 s[segstart] 的位置开始，搜索 IP 地址中的第 segid 段
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if segid == seg_count:  # 找到了4个段
                if segstart == len(s):  # 找完了所有字符
                    ipAddr = ".".join(str(seg) for seg in segments)
                    result.append(ipAddr)
                return
            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if segstart == len(s):  # 如果找完了所有字符，还没有4段，那就返回
                return
            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[segstart] == "0":
                segments[segid] = 0
                dfs(segid + 1, segstart + 1)
            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for segEnd in range(segstart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:  # 属于0-255的范围
                    segments[segid] = addr  # 作为一种可能加入
                    dfs(segid + 1, segEnd + 1)
                else:
                    break

        dfs(0, 0)
        return result


s = '25525511135'
Solution_restoreIpAddresses = Solution()
print(Solution_restoreIpAddresses.restoreIpAddresses(s))
