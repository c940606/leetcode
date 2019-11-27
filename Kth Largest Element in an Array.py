class Solution:
    def findKthLargest1(self, nums, k):
        """
        在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
        ---
        思路：
        集合 ---> 排序 --->找到
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest2(self, nums, k):
        n = len(nums)

        def adjust_heap(nums, i, max_len):
            # print("adjust front", nums)
            # i = 0
            tmp = i
            if i < max_len // 2:
                # print(i, nums)
                left = i * 2 + 1
                right = i * 2 + 2
                if left < max_len and nums[left] > nums[tmp]:
                    tmp = left
                if right < max_len and nums[right] > nums[tmp]:
                    tmp = right
                if tmp != i:
                    nums[tmp], nums[i] = nums[i], nums[tmp]
                    adjust_heap(nums, tmp, max_len)

            # print("adjust last", nums)

        for i in range((n - 2) // 2, -1, -1):
            # bulid_heap(i)
            # print(i)
            adjust_heap(nums, i, n)
            # print(nums)
        # print("bulid_head:", nums)
        res = None
        for i in range(1, k + 1):
            res = nums[0]
            # print("交换前", nums)
            nums[0], nums[-i] = nums[-i], nums[0]
            # print("交换后", nums)
            adjust_heap(nums, 0, n - i)
        # print("res", res)
        return res

    def findKthLargest3(self, nums, k):
        import heapq
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest(self, nums, k):
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1


# nums = [3,2,1,5,6,4]
# nums = [20, 50, 20, 40, 70, 10, 80, 30, 60]
k = 2
# nums1 = [-1,-1]
# k1 =2
a = Solution()
# print(a.findKthLargest(nums, k))
# print(a.findKthLargest([], 0))
# print(a.findKthLargest([3, 2, 1, 5, 6, 4], 2))
# print(a.findKthLargest([1, 2, 3, 4], 2))
print(a.findKthLargest([1, 3, 2, 5, 4, 8, 9, 6], 2))
# print(a.findKthLargest([1, 3, 5], 1))
# print(a.findKthLargest(
# [-1,2,0], 2))
