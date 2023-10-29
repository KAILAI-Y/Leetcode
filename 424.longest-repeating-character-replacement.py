#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#


# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # {char: count}, res
        # res = right - left + 1
        # l  r     window.length = r-l+1 = 3-0+1
        # AABABBA
        # the current window length, the max count of one char in the window
        # res - max(count) <= k
        # O(N)

        left = 0
        count = {}
        res = 0

        for right in range(len(s)):
            # add to sliding window
            count[s[right]] = count.get(s[right], 0) + 1

            while (right - left + 1) - max(count.values()) > k:
                # remove from window
                count[s[left]] -= 1

                left += 1

            res = max(res, right - left + 1)

        return res


# Validation:
# s = "AABABBA", k = 1
# left, right, count, res
# 0     0      {A: 1}  1
# 0     1      {A: 2}  2
# 0     2      {A: 2, B: 1}  3
# 0     3      {A: 3, B: 1}  4
# 0     4      {A: 3, B: 2}
#              {A: 2, B: 2}
# 1     5      {A: 2, B: 3}
#              {A: 1, B: 3}
# 2     5      {A: 1, B: 3}  4
# 2     6      {A: 2, B: 3}
#              {A: 2, B: 2}
# 3     6      {A; 1, B: 2}
# 4     6

# [A]ABABBA

# @lc code=end
