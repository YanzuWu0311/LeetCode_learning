import collections

"""
用哈希表记录每一个元素在哪一个列表中
再用bestLeft, bestRight表示最小区间的两端
再用left，right表示当前的区间
freq表示每个列表有几个数在区间内
inside表示有几个列表在区间内

当不是所有列表都在区间内，不断移动right，更新freq和inside
当所有列表都在到区间内
    若left，right比bestLeft, bestRight好，就替换
    否则bestLeft, bestRight不变
    开始移动left，更新freq，inside

直到right过界
"""


class Solution:
    def smallestRange(self, nums):
        n = len(nums)
        indices = collections.defaultdict(list)
        # 创建一个dict
        xMin, xMax = 10 ** 9, -10 ** 9
        # 所有元素的最大最小值
        for i, vec in enumerate(nums):  # 对输入的多个列表进行编号
            # print(i, vec)
            # 0 [4, 10, 15, 24, 26]
            # 1 [0, 9, 12, 20]
            # 2 [5, 18, 22, 30]
            for x in vec:
                # x表示vec列表中的每一个元素
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)
        # print(xMin)
        # print(xMax)
        # print(indices)
        # {4: [0],
        # 10: [0],
        # 15: [0],
        # 24: [0],
        # 26: [0],
        # 0: [1],
        # 9: [1],
        # 12: [1],
        # 20: [1],
        # 5: [2],
        # 18: [2],
        # 22: [2],
        # 30: [2]}
        # indices 里面存着每个元素是属于第几个列表的
        freq = [0] * n  # 表示每个列表里面的有几个数在区间内
        inside = 0  # 表示有几个列表已经包括在内
        left, right = xMin, xMin - 1
        # 当前区间的左右边界
        bestLeft, bestRight = xMin, xMax
        # bestLeft, bestRight表示最小区间的两端

        while right < xMax:
            right += 1
            if right in indices:  # 如果右边界在之前创建的字典中
                for x in indices[right]:  # 找出所有右边界所在的列表的index
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
Solution_smallestRange = Solution()
print(Solution_smallestRange.smallestRange(nums))
