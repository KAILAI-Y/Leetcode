#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True

        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[l1][l2]


# @lc code=end
