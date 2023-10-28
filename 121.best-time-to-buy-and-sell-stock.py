#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # two pointers
        # profit = prices[right] - prices[left]
        # if right number < left -> move left to current right position
        # update profit
        # O(N)
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return profit


# Validation:
# prices = [7,1,5,3,6,4]
# left right prices[left] prices[right] profit
# 0      1       7            1          0
# 1      2       1            5          4
# 1      3       1            3          2
# 1      4       1            6          5
# 1      5       1            4       max(5, 4)


# @lc code=end
