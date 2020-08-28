"""
找列表中两个字符串能组成一个回文，返回其index
哈希表，观察列表中每一个字符串s1，将其切开，分成前缀t1和后缀t2，
若前缀t1是回文，那么可以找一个新的字符串s2，s2是t2的翻转，s2+t1+t2；
若后缀t2是回文，则找一个s2是t1的翻转t1+t2+s2

"""
"""
超时了
class Solution(object):
    def palindromePairs(self, words):
        result = []
        length = len(words)
        for i in range(length):
            for j in range(length):
                str_temp = words[i] + words[j]
                if self.is_palindrome(str_temp) and i != j:
                    result.append([i, j])
        return result

    def is_palindrome(self, sentence):
        length = len(sentence)
        if length == 1 or length == 0:
            return True
        return sentence[0] == sentence[length - 1] and self.is_palindrome(sentence[1:length - 1])
"""


class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]
            # 正着读s和倒着读s是否相同
        words = {word: i for i, word in enumerate(words)}
        # 创建字典
        # words内容:index
        valid_pairs = []
        for word, k in words.items():  # 遍历每个单词
            n = len(word)
            for j in range(n + 1):  # 把每个单词从中间切开，分别找其对应的回文
                pref = word[:j]  # 前缀
                suf = word[j:]  # 后缀
                if is_palindrome(pref):  # 若前缀本身是回文
                    back = suf[::-1]  # 那他要找一个是该单词后缀的翻转
                    if back != word and back in words:
                        valid_pairs.append([words[back], k])
                if j != n and is_palindrome(suf):  # 若后缀是一个回文
                    back = pref[::-1]  # 则找一个前缀的翻转
                    if back != word and back in words:
                        valid_pairs.append([k, words[back]])
        return valid_pairs


words = ["bat", "tab", "cat"]
Solution_palindromePairs = Solution()
print(Solution_palindromePairs.palindromePairs(words))
