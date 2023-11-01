#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # -inf < root.val < inf
        # update to :
        # -inf < left.val < root.val
        # root.val < right.val < inf
        # dfs(root, left, right)

        def dfs(root, left, right):
            if not root:
                return True

            if not (right > root.val > left):
                return False

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        return dfs(root, float("-inf"), float("inf"))


# @lc code=end
