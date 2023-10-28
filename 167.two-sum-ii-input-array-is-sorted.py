#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointers: start & end exhaust both
        # if nums[i] + nums[j] > target -> j -= 1
        # else i += 1
        # return [i+1, j+1]
        # O(N)
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]


# Validation:
# numbers = [2,7,11,15], target = 9
# i, j, sum
# 0, 3, 17
# 0, 2, 13
# 0, 1, 9
# [1, 2]


# @lc code=end
