class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        res = []
        queue = []
        if not nums1 or not nums2:
            return []
        heapq.heappush(queue, (nums1[0] + nums2[0], (0, 0)))
        # print(queue)
        visited = {(0, 0)}
        while queue and len(res) < k:
            _, (i, j) = heapq.heappop(queue)
            res.append((nums1[i], nums2[j]))
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
        return res

    def kSmallestPairs1(self, nums1, nums2, k):
        import heapq
        queue = []
        if not nums1 or not nums2:
            return []
        for a in nums1:
            for b in nums2:
                heapq.heappush(queue,((a+b,(a,b))))
        return [tmp[1] for tmp in heapq.nsmallest(k,queue)]
        # print(heapq.nsmallest(k,queue))


a = Solution()
print(a.kSmallestPairs1(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
