#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start, combination, total):
            if total == target:
                ans.append(list(combination))
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # add the candidate to the current combination
                combination.append(candidates[i])

                # continue exploring with the updated combination and total
                backtrack(i + 1, combination, total + candidates[i])

                # remove the last element before the next iteration
                combination.pop()

        backtrack(0, [], 0)
        return ans


# @lc code=end
