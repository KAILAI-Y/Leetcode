#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS (root, maxValue)- pass the max root node value down
        # if children >= maxValue => count += 1
        # maxValue = max(maxValue, node.val)

        def dfs(node, maxValue):
            if not node:
                return 0

            res = 1 if node.val >= maxValue else 0
            maxValue = max(maxValue, node.val)
            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)

            return res

        return dfs(root, root.val)


# @lc code=end
