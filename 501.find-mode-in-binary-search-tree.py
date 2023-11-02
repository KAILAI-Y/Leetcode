#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # use dict to store count,
        # remember the maxCount of modes
        # return num if count equals to maxCount
        # O(N)
        def dfs(node):
            nonlocal max_count
            if not node:
                return
            dfs(node.left)

            # Update the count for the current number
            num = node.val
            count[num] = count.get(num, 0) + 1
            max_count = max(max_count, count[num])

            dfs(node.right)

        count = {}  # Dictionary to store counts
        max_count = 0  # Maximum count encountered

        # Perform in-order DFS traversal
        dfs(root)

        # Identify modes (numbers with counts equal to max_count)
        modes = [num for num, c in count.items() if c == max_count]

        return modes


# @lc code=end
