#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search:
        # if nums[mid] >= nums[l]  else
        # target in left  else: in right
        # Left:
        #  target < [l] or > [m] -> l moves to right else r to left
        # O(logn)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # LEFT
            if nums[mid] >= nums[l]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            # RIGHT
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


# @lc code=end
