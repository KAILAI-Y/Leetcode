#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # rows board[r]
        # cols board[r][c]
        # boxes idx = (r//3)* 3 + c//3 board[idx]
        # use set to store val in each rows, cols, boxes
        # to see if any number duplicate in each area
        # O(N^2)

        # initialize set list
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # iterate element in board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # check rows
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # check cols
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # check boxes
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


# @lc code=end
