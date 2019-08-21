class Solution(object):
    def longestConsecutive1(self, nums):
        """
        给定一个未排序的整数数组，找出最长连续序列的长度。
        要求算法的时间复杂度为 O(n)。
        ---
        输入: [100, 4, 200, 1, 3, 2]
        输出: 4
        解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                # print(num)
                y = num + 1
                while y in nums:
                    y += 1
                res = max(res, y - num)
        return res

    def longestConsecutive(self, nums):
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                # 判断左右是否可以连起来
                left = lookup[num - 1] if num - 1 in lookup else 0
                right = lookup[num + 1] if num + 1 in lookup else 0
                # 记录长度
                lookup[num] = left + right + 1
                # 把头尾都设置为最长长度
                if left:
                    lookup[num - left] = left + right + 1
                if right:
                    lookup[num + right] = left + right + 1
                res = max(res, left + right + 1)
        return res


a = Solution()
print(a.longestConsecutive([100, 4, 200, 1, 3, 2]))
