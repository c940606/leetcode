class Solution(object):
    def subsetsWithDup1(self, nums):
        """
        给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
        说明：解集不能包含重复的子集。
        ---
        输入: [1,2,2]
        输出:
        [
          [2],
          [1],
          [1,2,2],
          [2,2],
          [1,2],
          []
        ]
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        res = []

        def helper1(idx, n, temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                helper1(i + 1, n, temp_list + [nums[i]])

        def helper2(idx, n, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                helper2(i + 1, n, temp_list + [nums[i]])

        helper1(0, n, [])
        return res

    def subsetsWithDup(self, nums):
        if not nums: return []
        nums.sort()
        res = [[]]

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                tmp = len(res)
            for j in range(len(res) - tmp, len(res)):
                res.append(res[j] + [nums[i]])
        return res


a = Solution()
# print(a.subsetsWithDup([1, 2, 2]))
print(a.subsetsWithDup([4, 4, 4, 1, 4]))
