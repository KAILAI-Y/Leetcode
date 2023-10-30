#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # dict to store the original nodes and copies
        oldToCopy = {None: None}

        cur = head
        while cur:
            # create a node
            copy = Node(cur.val)
            # store the mapping
            oldToCopy[cur] = copy
            cur = cur.next

        # connect the copied nodes's next and random pointers
        cur = head
        while cur:
            # get the copy of the current node
            copy = oldToCopy[cur]
            # set the 'next' pointer of the copy to the copied version of the 'next' node.
            copy.next = oldToCopy[cur.next]
            # set the 'random' pointer of the copy to the copied version of the 'random' node.
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


# @lc code=end
