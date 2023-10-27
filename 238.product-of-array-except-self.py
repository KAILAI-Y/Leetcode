#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize two array left_product, right_product
        # for 2 in [1, 2, 3, 4], left_product = 1, right_product = 3*4, result = left_product * right_product
        # use ans[] to store left_product
        # start from the last num, get the right_product and result product by times ans
        # O(N)

        size = len(nums)
        ans = [0] * size

        ans[0] = 1
        for i in range(1, size):
            ans[i] = ans[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(size)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans


# Validations:
# [1,2,3,4]
# i: 1, 2, 3
# ans[i]: 1, 1, 2, 6
# i:  3, 2, 1, 0
# ans[i]: 6, 8, 12, 24
# R: 4, 12, 24, 24
# ans: [24, 12, 8, 6]


# @lc code=end
