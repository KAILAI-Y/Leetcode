#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, total, tank = 0, 0, 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0

        return start if total + tank >= 0 else -1


# @lc code=end
