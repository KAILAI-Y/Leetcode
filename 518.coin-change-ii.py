#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] [i's coin][amount]
        # not using: dp[i][j] = dp[i-1][j]
        # using: dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][amount]


# @lc code=end
