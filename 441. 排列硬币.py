"""
放置硬币，第n行放n个，给定总硬币数，求可以放几行
分治，low=0，high=n，计算mid和n-mid*（mid+1）/2的结果，判断是否要改变low，high的值，直至符合要求
"""


# 用binary search寻找值
class Solution(object):
    def arrangeCoins(self, n):
        """
        type: n int
        rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = int((low + high) / 2)
            if 0 <= n - (mid + 1) * mid / 2 < mid + 1:
                return mid
            elif n - (mid + 1) * mid / 2 >= mid + 1:
                low = mid + 1
            elif n - (mid + 1) * mid / 2 < 0:
                high = mid - 1


Solution_arrangeCoins = Solution()
result = Solution_arrangeCoins.arrangeCoins(3)
print(result)
