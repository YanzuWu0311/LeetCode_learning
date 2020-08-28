"""
字符串由0，1组成，找出所有字符串，符合要求①：0和1的数目相同②0和0在一起，1和1在一起
遍历字符串，统计连在一起的0（或1）的个数，两两取最小值即可
"""
"""
超时
class Solution(object):
    def countBinarySubstrings(self, s):

        result = 0
        result_array = []
        length = len(s)
        for i in range(length - 1):  # 最后一个字符肯定不行
            Flag = 1  # 默认在以i开始的地方可以找到
            if int(s[i]) == 0:  # 若当前指的是0
                zero_num = 1
                zero_index = i + 1
                while int(s[zero_index]) == 0 and zero_index <= length - 2:
                    zero_num += 1
                    zero_index += 1
                # 得到有几个0
                if zero_index + zero_num > length:
                    Flag = 0
                else:
                    if s[zero_index: zero_index+zero_num] == '1' * zero_num:
                        Flag = 1
                    else:
                        Flag = 0
                result += Flag
                if Flag == 1:
                    result_array.append([0]*zero_num + [1]*zero_num)

            else:  # 若当前指的是1
                one_num = 1
                one_index = i + 1
                while int(s[one_index]) == 1 and one_index <= length - 2:
                    one_num += 1
                    one_index += 1
                # 得到有几个1
                if one_index + one_num > length:
                    Flag = 0
                else:
                    if s[one_index: one_index + one_num] == '0' * one_num:
                        Flag = 1
                    else:
                        Flag = 0
                result += Flag
                if Flag == 1:
                    result_array.append([1]*one_num + [0]*one_num)
        return result
"""


# 我们可以将字符串 s 按照 0 和 1 的连续段分组，存在数组中，例如 s = 00111011，可以得到这样的数组：{2, 3, 1, 2}。 这里数组中两个相邻的数一定代表的是两种不同的字符。假设 数组中两个相邻的数字为 u
# 或者 v，它们对应着 u 个 0 和 v 个 1，或者 u 个 1 和 v 个 0。它们能组成的满足条件的子串数目为 min { u, v }，即一对相邻的数字对答案的贡献。
#
# 我们只要遍历所有相邻的数对，求它们的贡献总和，即可得到答案


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 1
        num_array = []
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                num += 1
            else:
                num_array.append(num)
                num = 1
        num_array.append(num)
        for i in range(len(num_array) - 1):
            result += min(int(num_array[i]), int(num_array[i+1]))
        return result


s = '00110011'
Solution_countBinarySubstrings = Solution()
print(Solution_countBinarySubstrings.countBinarySubstrings(s))
