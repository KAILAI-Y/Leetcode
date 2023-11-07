# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # calculate the sum of the num array , if even -> can be split to two
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


# @lc code=end
