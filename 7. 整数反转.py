"""
把输入的数字反过来，123变为321
整除10，余数
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        decompose_num = []
        num = x

        # 判断正负
        if num >= 0:
            flags = 1
        else:
            flags = -1
            num = flags * num

        while num != 0:
            shang, yu_shu = divmod(num, 10)
            num = (num - yu_shu) / 10
            decompose_num.append(int(yu_shu))

        result = 0

        for _ in decompose_num:
            result *= 10
            result += _
        result = result * flags
        return result if 2 ** 31 > result >= -2 ** 31 else 0


x = 123
Solution_reverse = Solution()
print(Solution_reverse.reverse(x))
