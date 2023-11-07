#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or (target + total) % 2 == 1:
            return 0

        target = (target + total) // 2
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]

        return dp[n][target]


# @lc code=end
