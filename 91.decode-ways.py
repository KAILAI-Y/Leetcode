#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # dp[i] will store the total number of decode ways up to index i-1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1  # since we've already handled s[0] != '0' case

        for i in range(2, len(s) + 1):
            # If the current character is not '0', it can be decoded on its own
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]

            # Check if the current and the previous character together can be decoded
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


# @lc code=end
