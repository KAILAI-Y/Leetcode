#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_so_far = min_so_far = global_max = nums[0]

        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])

            max_so_far = temp_max

            global_max = max(global_max, max_so_far)

        return global_max


# @lc code=end
