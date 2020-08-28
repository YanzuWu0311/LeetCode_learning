"""
找到两个排好序的列表的中间数
把两个列表合并，也是有序的即可
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_total = []
        index1 = 0
        index2 = 0
        m = len(nums1)
        n = len(nums2)
        while index1 < m and index2 < n:
            if nums1[index1] <= nums2[index2]:
                num_total.append(nums1[index1])
                index1 += 1
            else:
                num_total.append(nums2[index2])
                index2 += 1
        if index1 < m:
            for i in range(index1, m):
                num_total.append(nums1[i])
        elif index2 < n:
            for i in range(index2, n):
                num_total.append(nums2[i])
        len_total = len(num_total)
        if len_total % 2 == 0:
            return float((num_total[int(len_total / 2) - 1] + num_total[int(len_total / 2)]) / 2.0)
        else:
            return float(num_total[int(len_total / 2)])


nums1 = [1, 2]
nums2 = [3, 4]
Solution_findMedianSortedArrays = Solution()
result = Solution_findMedianSortedArrays.findMedianSortedArrays(nums1, nums2)
print(result)
