"""
找出原字符串中最长的没有字母重复的字串
多指针，用两个指针，分别指向字串的头和尾，未发现重复字母，头指针右移，发现重复字母，左指针右移，直至字串里面没有重复字母
"""


class Solution(object):
    """
    左右两个指针，一开始都指向s的首位
    右指针不断往后走，把元素加到集合中
    直到遇到一个重复的元素
    这时候左指针按s中的顺序依次删去元素，直到可以让右指针指向的元素放入集合中
    求整个过程中集合的最多元素个数
    """

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        chars = set()  # 集合
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in chars:
                if s[left] in chars:
                    chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))
        return res


seq = "pwwkew"
Solution_lengthOfLongestSubstring = Solution()
result = Solution_lengthOfLongestSubstring.lengthOfLongestSubstring(seq)
print(result)
