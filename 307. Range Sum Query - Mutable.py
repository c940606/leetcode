from 数据结构.树状数组 import BIT


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.tree = BIT(nums)

    def update(self, i: int, val: int) -> None:
        self.tree.updata(i, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.prefix(j) - self.tree.prefix(i - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
