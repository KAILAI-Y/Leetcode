#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        while count:
            min_card = min(count)  # find the smallest card
            for card in range(min_card, min_card + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    del count[card]

        return True


# @lc code=end
