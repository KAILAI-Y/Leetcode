#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#


# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                # skip the duplicate element
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # update current state
                path.append(nums[i])
                backtrack(i + 1, path)
                # remove last added
                path.pop()

        backtrack(0, [])
        return res


# @lc code=end
