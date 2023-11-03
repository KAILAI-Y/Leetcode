#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, path):
            if i == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = phone_map[digits[i]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(i + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations


# @lc code=end
