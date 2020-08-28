"""
打印所有集合的子集
迭代法，一开始只有空集，选中一个原集合的数，不断和之前的集合合并添加到最终的集合中
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            for element in result[:]:
                # new = old[:] 复制列表，不然若直接new = old,修改new也会修改old
                x = element[:]
                x.append(num)
                result.append(x)
        return result


s = [1, 2, 3]
Solution_subsets = Solution()
print(Solution_subsets.subsets(s))
