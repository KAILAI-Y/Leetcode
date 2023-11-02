#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#


# @lc code=start
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # calculate the distance
        # [distance, x, y]
        # heapify ,
        # While k: heappop get distance, x, y
        # res.append( [x, y] ) when k = 0

        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)

        res = []
        while k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            print(res)
            k -= 1

        return res


# @lc code=end
