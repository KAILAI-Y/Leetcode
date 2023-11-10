#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = max_open = 0
        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open = max(0, min_open - 1)
                max_open -= 1
                if max_open < 0:
                    return False
            else:  # c == '*'
                min_open = max(0, min_open - 1)
                max_open += 1

        return min_open == 0


# @lc code=end
