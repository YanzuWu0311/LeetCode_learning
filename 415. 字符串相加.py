"""
把两个字符串当作数字相加。结果返回
字符串，从最低位开始计算，两两相加，设置一个进位位，表示是否进位
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1 = len(num1)
        length2 = len(num2)
        length = max(length1, length2)
        # 先把短的补齐
        if length1 > length2:
            num2 = '0' * (length1 - length2) + num2
        else:
            num1 = '0' * (length2 - length1) + num1

        flag = 0
        # 初始化进位标志为0
        result = []
        result_str = ''
        for index in range(length - 1, -1, -1):
            temp1 = int(num1[index])
            temp2 = int(num2[index])
            temp_sum = temp1 + temp2 + flag
            if temp_sum > 9:
                # 需要进位
                flag = 1
                temp_sum -= 10
                result.append(temp_sum)
            else:
                flag = 0
                result.append(temp_sum)
        if flag == 1:
            result.append(1)
        result.reverse()
        for num in result:
            result_str += str(num)
        return result_str


num1 = '1'
num2 = '9'
Solution_addStrings = Solution()
print(Solution_addStrings.addStrings(num1, num2))
