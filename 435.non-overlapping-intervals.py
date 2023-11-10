#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        count = 0
        end = intervals[0][1]

        for intervals in intervals[1:]:
            if intervals[0] < end:
                count += 1
            else:
                end = intervals[1]

        return count


# @lc code=end
