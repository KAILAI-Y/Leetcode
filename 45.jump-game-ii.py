#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        maxPosition = 0
        steps = 0

        for i in range(n - 1):
            maxPosition = max(maxPosition, i + nums[i])
            if i == end:
                end = maxPosition
                steps += 1

        return steps


# @lc code=end
