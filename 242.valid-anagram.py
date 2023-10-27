#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#


# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # len(s) != len(t) -> False
        # use dict to count frequency of s {char: count}: {'a': 2}
        # iterate t: if t-char not in dict -> false; if t-char in dict ->  count - 1; if count == 0 -> del char in dict
        # True if s_dict empty: not(s_dict)
        # O(N)

        if len(s) != len(t):
            return False

        s_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
                if s_dict[char] == 0:
                    del s_dict[char]
            else:
                return False

        return False if len(s_dict) else True

        # dict[""] = count


# Validation:
# s="anagram" t="nagaram"
# s_dict = {"a": 3, "n": 1, "g": 1, "r": 1, "m": 1}
# n {"a": 3, "g": 1, "r": 1, "m": 1}
# a {"a": 2, "g": 1, "r": 1, "m": 1}
# g {"a": 2, "r": 1, "m": 1}
# a {"a": 1, "r": 1, "m": 1}
# r {"a": 1, "m": 1}
# a {"m": 1}
# m {}
# True


# @lc code=end
