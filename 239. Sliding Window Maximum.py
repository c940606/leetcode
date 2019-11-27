class Solution:
    def maxSlidingWindow1(self, nums, k):
        """
        用一个队列 保持 索引号 < k
        一直和队列头比较, 让小的弹出来
        :param nums:
        :param k:
        :return:
        """
        from collections import deque
        queue = deque()
        queue.extendleft()
        res = []
        for i in range(len(nums)):
            if queue and i - queue[0] + 1 > k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i - k + 1 >= 0:
                res.append(nums[queue[0]])
        return res

    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        n = len(nums)
        left_max = [0] * n
        left_max[0] = nums[0]
        right_max = [0] * n
        right_max[-1] = nums[-1]
        res = []
        for i in range(1, n):
            left_max[i] = nums[i] if i % k == 0 else max(left_max[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = nums[i] if i % k == 0 else max(right_max[i + 1], nums[i])
        i = 0
        while i + k - 1 < n:
            res.append(max(right_max[i], left_max[i + k - 1]))
            i += 1
        return res

a = Solution()
print(a.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
