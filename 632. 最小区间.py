"""
找出一个最小区间，包含所有列表中各至少一个元素
多指针，每个列表分配一个指针，最小值所在列表的指针右移
"""


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        list_num = len(nums)
        current_list_index = []  # 该列表存着指向每个列表的指针
        end_list = []
        for i in range(list_num):
            current_list_index.append(0)
            end_list.append(0)
        for i in range(list_num):  # 若一开始一个列表只有一个数字，那就直接置1
            if len(nums[i]) == 1:
                end_list[i] = 1
        # 初始化都指向最开始
        result_dict = {}

        while 1:
            temp_list = []

            for i in range(list_num):
                new_ele = nums[i][current_list_index[i]]
                temp_list.append(new_ele)
            right = max(temp_list)
            left = min(temp_list)
            width = right - left
            if width not in result_dict:
                result_dict[width] = (left, right)
            else:
                old_left, old_right = result_dict[width]
                if left < old_left:
                    result_dict[width] = (left, right)

            # 把三个列表中最小的数的那个列表，要右移
            move_list = []
            min_index = -1
            min_value = 10 ** 6
            for i in range(list_num):
                if end_list[i] == 0:
                    # 还没走到底
                    move_list.append(nums[i][current_list_index[i]])
                else:
                    # 走到底
                    move_list.append(10 ** 6)
            for i in range(list_num):
                if move_list[i] < min_value:
                    min_value = move_list[i]
                    min_index = i
            if end_list[min_index] == 0:
                current_list_index[min_index] += 1
                if current_list_index[min_index] + 1 == len(nums[min_index]):
                    end_list[min_index] = 1
            else:
                break

        min_width = 10 ** 5
        for _ in result_dict:
            min_width = min(min_width, _)
        return result_dict[min_width]


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
Solution_smallestRange = Solution()
print(Solution_smallestRange.smallestRange(nums))
