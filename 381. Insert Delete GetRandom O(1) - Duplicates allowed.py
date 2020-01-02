import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = defaultdict(list)
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = True
        if val in self.lookup:
            flag = False
        self.lookup[val].append(len(self.nums))
        self.nums.append(val)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        if not self.lookup[val]:
            return False
        loc = self.lookup[val].pop()
        num = self.nums[-1]
        self.nums[loc] = num
        if self.lookup[num]:
            self.lookup[num].append(loc)
            self.lookup[num].remove(len(self.nums) - 1)
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# ["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]
# [[],[1],[1],[2],[],[1],[]]
