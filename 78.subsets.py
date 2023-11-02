#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#


# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        ans.append([])

        def backtrack(start, sub):
            for i in range(start, len(nums)):
                sub.append(nums[i])
                ans.append(list(sub))
                backtrack(i + 1, sub)
                sub.pop()

        backtrack(0, [])
        return ans


# @lc code=end
