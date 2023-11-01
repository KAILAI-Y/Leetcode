#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])  # get index
        root.left = self.buildTree(
            preorder[1 : mid + 1], inorder[:mid]
        )  # Recursively build the left subtree: left's left
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


# @lc code=end
