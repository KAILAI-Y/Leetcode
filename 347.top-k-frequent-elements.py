#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#


# @lc code=start
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Edge case: if k = len(nums) -> nums
        # Top k -> Heap
        # Method count the frequency O(N·logk)
        # Count the frequency of each number using a dictionary
        freq = Counter(nums)

        # Sort the dictionary by values in descending order and keys in ascending order in case of a tie
        # negates the frequency (item[1]) of each number
        sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
        print(sorted_freq)

        # Take the first k items to get the top k frequent elements
        top_k = [x[0] for x in sorted_freq[:k]]
        print(top_k)

        return top_k


# Validation:
# nums = [4,1,-1,2,-1,2,3] k = 2
# freq = {2: 2, -1: 2, 1: 1, 3: 1, 4: 1}
# sorted_freq = [(-1, 2), (2, 2), (1, 1), (3, 1), (4, 1)]
# top_k [-1, 2]


# @lc code=end
