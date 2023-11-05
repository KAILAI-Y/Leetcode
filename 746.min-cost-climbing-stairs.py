#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # base case
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])


# @lc code=end
