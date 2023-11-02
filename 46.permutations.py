#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(curr):
            # base case: if current permutation has same length as input
            if len(curr) == len(nums):
                permutations.append(curr[:])
                return

            for num in nums:
                # skip numbers that are already in the curr
                if num in curr:
                    continue
                # update curr
                curr.append(num)
                backtrack(curr)
                # remove last added
                curr.pop()

        backtrack([])
        return permutations


# @lc code=end
