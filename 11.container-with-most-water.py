#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#


# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # calculate area: base (j - i) * height (min(height[i], height[j]))
        # update maxArea: max(maxArea, area)

        i = 0
        j = len(height) - 1
        maxArea = 0

        while i < j:
            area = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, area)

            # moving the short line's pointer turn out to be beneficial
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea


# @lc code=end
