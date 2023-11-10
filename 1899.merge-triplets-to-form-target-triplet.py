#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#


# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [0, 0, 0]

        for triplet in triplets:
            if (
                triplet[0] <= target[0]
                and triplet[1] <= target[1]
                and triplet[2] <= target[2]
            ):
                current = [
                    max(current[0], triplet[0]),
                    max(current[1], triplet[1]),
                    max(current[2], triplet[2]),
                ]

        return current == target


# @lc code=end
