#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # edge case: if input is empty string, len = 1
        # iterate strs, for char in strs[i] {str: list}
        # use tuple as key since it's immutable
        # or use sorted str as key
        # sorted_str = ''.join(sorted(str))
        # sorting O(klogk) for str in strs
        # iterate N length list
        # =>O(N·klogk)
        ans = collections.defaultdict(list)
        for str in strs:
            ans[tuple(sorted(str))].append(str)
        return ans.values()


# strs = ["eat","tea","tan","ate","nat","bat"]
# {
# ('a', 'e', 't'): ['eat', 'tea', 'ate'],
# ('a', 'n', 't'): ['tan', 'nat'],
# ('b', 'a', 't'): ['bat']
# }

# {
# "aet": ['eat', 'tea', 'ate'],
# "ant": ['tan', 'nat'],
# "bat": ['bat']
# }


# @lc code=end
