#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#


# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # edge case: the smallest num > 0
        # O(nlogn + n^2)
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            # avoid duplicate
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)

        return res

    # nums[i] + nums[j] + nums[k]
    # two pointers: j, k
    def twoSumII(self, nums, i, res):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                # avoid duplicates
                while j < k and nums[j] == nums[j - 1]:
                    j += 1


# @lc code=end
