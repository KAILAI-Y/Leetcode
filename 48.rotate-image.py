# @before-stub-for-debug-begin
from python3problem48 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 转置矩阵
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 反转每一行
        for i in range(n):
            matrix[i].reverse()


# @lc code=end
