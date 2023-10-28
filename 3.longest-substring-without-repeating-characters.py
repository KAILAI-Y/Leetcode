#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import Counter


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window: use set to store seen char
        # remove the left char from set to avoid duplicate
        left = 0
        charSet = set()
        res = 0

        for right in range(len(s)):
            # sliding window broken condition
            while s[right] in charSet:
                # remove arr[left]
                charSet.remove(s[left])
                left += 1

            # add arr[right]
            charSet.add(s[right])

            # update answer
            res = max(res, right - left + 1)

        return res


# Validation:
# "abcabcbb"
# left,  right, charSet, res
# 0       -       {}      0
# 0       0      {a}      1
# 0       1     {a, b}    2
# 0       2    {a, b, c}  3
# 0       3    {b, c}
# 1       3    {b, c, a}  3
# 1       4    {c, a}
# 2       4    {c, a, b}  3
# 2       5    {a, b}
# 3       5    {a, b, c}  3
# 3       6    {b, c}
# 4       6    {c}
# 5       6    {c, b}    max(3, 2)
# 5       7    {b}
# 6       7    {}
# 7       7    {b}      max(3, 1)
# @lc code=end
