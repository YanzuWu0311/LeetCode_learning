"""
找最大乘水量
使用首尾指针，计算此时的盛水量，之后看左右哪个高度小，高度小的放弃，往里走一个
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left_point = 0
        right_point = len(height) - 1
        while left_point < right_point:
            water = (right_point - left_point) * min(height[left_point], height[right_point])
            max_water = max(max_water, water)
            if height[left_point] < height[right_point]:
                left_point += 1
            else:
                right_point -= 1
        return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Solution_maxArea = Solution()
print(Solution_maxArea.maxArea(height))
