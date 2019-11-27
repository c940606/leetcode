from typing import List


class Solution:
    def maxNumber1(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        self.res = 0

        def helper(i, j, k, num):
            # print(i, j, k, num)
            if (n1 - i) + (n2 - j) < k:
                return
            if k == 0:
                # print(num)
                self.res = max(self.res, num)
            if i < n1 and j < n2:
                helper(i + 1, j + 1, k, num)
                if nums1[i] > nums2[j]:
                    helper(i + 1, j, k - 1, num * 10 + nums1[i])
                elif nums1[i] <= nums2[j]:
                    helper(i, j + 1, k - 1, num * 10 + nums2[j])
            if i < n1:
                helper(i + 1, j, k, num)
                helper(i + 1, j, k - 1, num * 10 + nums1[i])
            if j < n2:
                helper(i, j + 1, k, num)
                helper(i, j + 1, k - 1, num * 10 + nums2[j])

        helper(0, 0, k, 0)
        return self.res

    def maxNumber2(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """
        1. 两个数组 i个 另一个取 k - i个
        2. 一个数组 k 位
        :param nums1:
        :param nums2:
        :param k:
        :return:
        """

        def getMaxArr(nums, i):
            n = len(nums)
            if i == 0:
                return []
            stack = []
            for loc, num in enumerate(nums):
                # print(stack, loc, num)
                while stack and stack[-1] < num and i - len(stack) != n - loc:
                    stack.pop()
                if len(stack) < i:
                    stack.append(num)
            return stack

        # print(getMaxArr(nums1, 4))
        def merger(tmp1, tmp2):
            # print(tmp1, tmp2)
            ans = []
            i = 0
            j = 0
            while i < len(tmp1) and j < len(tmp2):
                if tmp1[i:] > tmp2[j:]:
                    ans.append(tmp1[i])
                    i += 1
                else:
                    ans.append(tmp2[j])
                    j += 1
            ans.extend(tmp1[i:])
            ans.extend(tmp2[j:])
            return ans

        res = [0] * k
        for i in range(len(nums1) + 1):
            tmp1 = getMaxArr(nums1, i)
            tmp2 = getMaxArr(nums2, k - i)
            if len(tmp1) + len(tmp2) != k: continue
            # print(tmp1, tmp2)
            tmp = merger(tmp1, tmp2)
            # print(tmp)
            if res < tmp:
                res = tmp
        return res

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def getMaXArr(nums, i):
            n = len(nums)
            if i == 0:
                return []
            stack = []
            for loc, num in enumerate(nums):
                # print(stack, loc, num)
                while stack and stack[-1] < num and i - len(stack) != n - loc:
                    stack.pop()
                if len(stack) < i:
                    stack.append(num)
            return stack

        def merge(tmp1, tmp2):
            # print(len(tmp1) + len(tmp2))
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        # res = [0] * k
        # # print(len(nums1), len(nums2))
        # for i in range(k + 1):
        #     if i <= len(nums1) and k - i <= len(nums2):
        #         # print(i, k - i)
        #         tmp1 = getMaXArr(nums1, i)
        #         tmp2 = getMaXArr(nums2, k - i)
        #         # print(len(tmp1), len(tmp2))
        #         tmp = merge(tmp1, tmp2)
        #         if res < tmp:
        #             res = tmp
        # return res
        return max(merge(getMaXArr(nums1, i), getMaXArr(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))


a = Solution()
print(a.maxNumber(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    , 200))
# print(a.maxNumber([2, 3], [8], 3))
# print(a.maxNumber(nums1=[3, 4, 6, 5], nums2=[9, 1, 2, 5, 8, 3], k=5))
# print(a.maxNumber(nums1=[3, 9], nums2=[8, 9], k=3))
# print(a.maxNumber(nums1=[6, 7], nums2=[6, 0, 4], k=5))
# print(a.maxNumber([6, 7], [6, 0, 4], 5))
# print(a.maxNumber([5, 6, 8], [6, 4, 0], 3))
