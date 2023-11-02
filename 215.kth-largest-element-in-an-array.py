#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#


# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)

        res = 0
        while k > 0:
            num = heapq.heappop(nums)
            res = -1 * (num)
            k -= 1

        return res


# @lc code=end
