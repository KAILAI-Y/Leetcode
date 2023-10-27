#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#


# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Final return what if non-exist?
        # input array is not sorted
        # hashmap {}, store all number in set hashmap[nums[i]] = i
        # iterate i, complement = target - nums[i]
        # if complement in set: -> [i, set[complement]]
        # O(N) traverse list once

        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


# Validation:
# nums = [2,7,11,15], target = 9
# i complement hashmap
# 0  7          {2: 0}
# 1  2          return [1, 0]
# 2
# 3

# @lc code=end
