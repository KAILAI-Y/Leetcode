#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # use two pointers, calculate the trapped water based on the difference between the leftMax, rightMax and new position
        # if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right).
        # As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
        # O(N)
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            # leftMax < rightMax -> higher pillar height in the right; can store rainwater between
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


# Validation:
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# l  r  height[l] height[r] leftMax rightMax  res
# 0 11   0           1         0        1      0
# 1 11   1           1         1        1      0
# 1 10   1           2         1        2      0
# 2 10   0           2         1        2      1
# 3 10   2           2         2        2      0
# 3  9   2           1         2        2      1
# 3  8   2           2         2        2      0
# 3  7   2           3         2        3      0
# 4  7   1           3         2        3      1
# 5  7   0           3         2        3      2
# 6  7   1           3         2        3      1
# sum(res) = 6

# @lc code=end
