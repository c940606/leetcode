class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        from itertools import combinations
        self.lookup = [s for s in combinations("".join(sorted(characters)), combinationLength)]
        self.i = 0

    def next(self) -> str:
        tmp = self.lookup[self.i]
        self.i += 1
        return tmp

    def hasNext(self) -> bool:
        return self.i < len(self.lookup)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()