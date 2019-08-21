class Solution:
    def getSkyline(self, buildings):
        import heapq
        res = []
        height = []
        for b in buildings:
            height.append([b[0], -b[2]])
            height.append([b[1], b[2]])
        height.sort()
        #print(height)
        heap = [0]
        pre = 0
        for h in height:
            if h[1] < 0:
                heapq.heappush(heap, h[1])
            else:
                heap.remove(-h[1])
                heapq.heapify(heap)
            cur = -heap[0]
            if pre != cur:
                res.append([h[0], cur])
                pre = cur
        return res


a = Solution()
print(a.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(a.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
