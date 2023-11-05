#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def rob_linear(houses):
            prev_max, curr_max = 0, 0
            for amount in houses:
                prev_max, curr_max = curr_max, max(prev_max + amount, curr_max)
            return curr_max

        # 0 -> n-2
        rob1 = rob_linear(nums[:-1])
        # 1 -> n-1
        rob2 = rob_linear(nums[1:])

        return max(rob1, rob2)


# @lc code=end
