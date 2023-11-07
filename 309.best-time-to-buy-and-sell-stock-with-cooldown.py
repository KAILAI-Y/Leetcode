#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j] [day][hold or not] 1: hold 0: not hold
        # not hold: dp[i][0]  dp[i-1][0] or dp[i-1][1] +prices[i]
        # dp[i][1] dp[i-1][1] or dp[i-2][0]-prices[i]
        # dp[0][0] = 0 dp[0][1] = -prices[0]

        # prices less than 2, no need to buy
        if len(prices) < 2:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]  # [i][0]: not hold stock [i][1]: hold stock

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # not hold: 1. i-1 day not hold 2. i-1 day hold but sold
        # hold: 1. i-1 day hold 2. i-2day buy a stock i-1 is cooldown
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n - 1][0]


# @lc code=end
