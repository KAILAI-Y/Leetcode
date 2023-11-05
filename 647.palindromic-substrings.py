#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # base case: single letter substring
        for i in range(n):
            dp[i][i] = True
            count += 1

        # base case: double letters substring
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # general case:
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    count += 1

        return count


# @lc code=end
