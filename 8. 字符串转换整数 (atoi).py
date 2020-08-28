"""
按照一定的规律把字符串通过筛选生成纯数字
按照要求进行if判别
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag = 1
        dig = []
        index = 0
        result = 0
        if len(str) == 0:
            return 0
        for char in str:  # 去掉之前的空格
            if char == ' ':
                index += 1
            else:
                break
        if index == len(str):
            return 0
        if str[index] == '-':  # 判断正负号
            flag = -1
            index += 1
        elif str[index] == '+':
            index += 1
        for i in range(index, len(str)):
            if str[i].isdigit():
                new_num = str[i]
                dig.append(new_num)
            else:
                break
        for i in range(len(dig)):
            result *= 10
            result += int(dig[i])
        result = result * flag
        if result >= 2 ** 31:
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31
        else:
            return result


input = '4193 with words'
Solution_myAtoi = Solution()
print(Solution_myAtoi.myAtoi(input))
