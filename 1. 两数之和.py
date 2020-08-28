"""
找到一个列表里面和为目标值的两个数的index
利用hash表查找另一个数的index
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        # print(hashmap)
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


numbers = [2, 7, 11, 13]
target = 9
Solution_twosum = Solution()
result = Solution_twosum.twoSum(numbers, target)
print(result)
