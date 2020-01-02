import random
import time
time.time()
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.lookup: return False
        self.lookup[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.lookup: return False
        loc = self.lookup[val]
        # 最后一个替换
        self.nums[loc], self.nums[-1] = self.nums[-1], self.nums[loc]
        self.lookup[self.nums[loc]] = loc
        # 字典 和 列表删除最后一个
        self.lookup.pop(self.nums.pop())
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
