#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        result = []

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    result.append(matrix[bottom][col])
                for row in range(bottom, top, -1):
                    result.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result


# @lc code=end
