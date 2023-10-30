#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow => mid

        # reverse second half
        curr = slow.next
        prev = slow.next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        print(prev)

        # merge two halves
        first, second = head, prev
        # print(first, second)
        # print(second.next)
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# @lc code=end
