#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, combination, total):
            if total == target:
                ans.append(list(combination))
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # add the candidate to the current combination
                combination.append(candidates[i])

                # continue exploring with the updated combination and total
                backtrack(i, combination, total + candidates[i])

                # remove the last element before the next iteration
                combination.pop()

        backtrack(0, [], 0)
        return ans


# @lc code=end
