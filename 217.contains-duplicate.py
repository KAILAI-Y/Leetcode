#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashmap
        # O(N) iterate list insert to set
        nums_set = set(nums)
        return not (len(nums_set) == len(nums))


# @lc code=end
