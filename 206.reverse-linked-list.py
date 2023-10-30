#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # T O(N) M O(1)
        # curr = head
        # prev = None

        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next

        # return prev

        # T O(N) M O(N)
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead


# @lc code=end
