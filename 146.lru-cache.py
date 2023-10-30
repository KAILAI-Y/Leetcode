#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


# Double LinkedList
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}  # map key to node

        # left = LRU, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        # connect
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    # prev node nxt --> prev nxt
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    # prev right --> prev node right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU form the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
