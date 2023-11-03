#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Cols = len(board), len(board[0])

        def backtrack(r, c, index):
            # base case
            # index == word length
            if index == len(word):
                return True

            # check boundaries and if char match
            if r < 0 or c < 0 or r >= Rows or c >= Cols or word[index] != board[r][c]:
                return False

            # save the character and mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore in all 4 directions
            found = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )

            # revert state
            board[r][c] = temp

            return found

        for i in range(Rows):
            for j in range(Cols):
                if backtrack(i, j, 0):
                    return True

        return False


# @lc code=end
