#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS Recursion
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # DFS Iterative
        stack = [root, 1]
        level = 0

        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return level

        # BFS
        # if not root:
        #     return 0
        # queue = deque([root])
        # level = 0

        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1

        # return level


# @lc code=end
