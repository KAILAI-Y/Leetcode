#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#


# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # edge case: no stone, only one stone
        # use maxHeap -> transfer nums into negative then use minHeap
        # while len(heap) > 1: need two to compare
        # pop first, second, push first - second
        # return abs(stone[0])
        # if len(stones) == 1:
        #     return stones[0]

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        return abs(stones[0]) if stones else 0


# @lc code=end
