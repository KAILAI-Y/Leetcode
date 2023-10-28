#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case:
        #       nums is empty -> 0
        #       duplicate element
        # set list and sort
        # count themself: count = 1, current_count = 1
        # iterate from i = 1
        # nums[i-1] == nums[i] - 1 -> current_count  += 1
        # reset the current_count when consecutive break
        # count = max(count, current_count)
        # O(n·logn) for sorting

        # sorted_nums = sorted(set(nums))
        # count = 1
        # current_count = 1

        # for i in range(1, len(sorted_nums)):
        #     if sorted_nums[i - 1] == sorted_nums[i] - 1:
        #         current_count += 1
        #     else:
        #         current_count = 1
        #     print(current_count)
        #     count = max(count, current_count)

        # return 0 if len(nums) == 0 else count

        # remove sorting, use set to check if the num[i-1] in the set
        # O(N) for while
        nums_set = set(nums)
        count = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_count = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_count += 1

                count = max(count, current_count)

        return count


# Validation:
# [9,1,4,7,3,-1,0,5,8,-1,6]
# [-1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
# 1 2 3 1 2 3 4 5 6 7


# @lc code=end
