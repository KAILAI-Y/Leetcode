#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # use two index
        # O(N) traverse array once
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex


# [1, 1, 2]
#  i  nums[i-1] nums[i]   nums[insertIndex]  insertIndex  nums
#  1     1        1                               1      [1, 1, 2]
#  2     1        2        1-> 2                  3      [1, 2, 2]


# @lc code=end
