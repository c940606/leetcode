from typing import List

from 数据结构.树状数组 import BinaryIndexedTree as BIT
from 数据结构.线段树 import SegmentTree


class Solution:
    def countSmaller1(self, nums):
        import bisect
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]

    def countSmaller2(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        arr = []
        for idx, num in enumerate(nums):
            arr.append((idx, num))

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            i = 0
            j = 0
            # print(left, right, res)
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    arr[i + j] = left[i]
                    res[left[i][0]] += j
                    i += 1
                else:
                    arr[i + j] = right[j]
                    j += 1
            return arr

        mergeSort(arr)
        return res

    def countSmaller3(self, nums: List[int]) -> List[int]:

        arr = []
        res = [0] * len(nums)
        for idx, num in enumerate(nums):
            arr.append((idx, num))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            # print(left, right)
            return merge(left, right)

        def merge(left, right):
            tmp = []
            i = 0
            j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    tmp.append(left[i])
                    res[left[i][0]] += j
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            return tmp

        merge_sort(arr)
        return res

    def countSmaller5(self, nums: List[int]) -> List[int]:
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        # print(hashTable)
        tree = BIT([0] * len(hashTable))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.prefix(hashTable[nums[i]]))
            tree.updata(hashTable[nums[i]], 1)
        return res[::-1]

    def countSmaller6(self, nums: List[int]) -> List[int]:
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree, r = SegmentTree(len(hashTable) * [0]), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sumRange(0, hashTable[nums[i]] - 1))
            tree.updata(hashTable[nums[i]], 1)
        return r[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:

        def insert(node, val):
            Sum = 0
            while node.val != val:
                if node.val > val:
                    if node.left == None:
                        node.left = Node(val)
                    node.leftSum += 1
                    node = node.left
                else:
                    Sum += node.leftSum + node.dup
                    if node.right == None:
                        node.right = Node(val)
                    node = node.right
            node.dup += 1
            return Sum + node.leftSum

        res = [0] * len(nums)
        root = Node(nums[-1])
        for i in range(len(nums) - 1, -1, -1):
            res[i] = insert(root, nums[i])
        return res


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.leftSum = 0
        self.dup = 0


a = Solution()
print(a.countSmaller([-1, -1]))
print(a.countSmaller([5, 2, 6, 1]))
print(a.countSmaller(
    [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97, 3,
     76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]))
# print(a.countSmaller([2, 0, 1]))
# print(a.countSmaller([]))
