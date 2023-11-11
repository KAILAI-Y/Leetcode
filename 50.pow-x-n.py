#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                ans = ans * current_product
            current_product *= current_product
            n = n // 2

        return ans


# @lc code=end
