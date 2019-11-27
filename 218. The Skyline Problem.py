class Solution:
    def getSkyline1(self, buildings):
        import heapq
        res = []
        height = []
        for b in buildings:
            height.append([b[0], -b[2]])
            height.append([b[1], b[2]])
        height.sort()
        # print(height)
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

    def getSkyline2(self, buildings):
        import bisect
        res = [[0, 0]]
        # 记录 [left, height], [right, height]
        loc = []
        for l, r, h in buildings:
            # 为了排序让 left那边靠前, 所以让高度取负
            loc.append([l, -h])
            loc.append([r, h])
        loc.sort()
        heap = [0]

        for x, h in loc:
            if h < 0:
                # 默认最小堆, 加符号变成最大堆
                bisect.insort(heap, h)
            else:
                heap.remove(-h)
            cur = -heap[0]
            if res[-1][1] != cur:
                res.append([x, cur])

        return res[1:]

    def getSkyline3(self, buildings):
        if not buildings: return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    # 两个合并
    def merge(self, left, right):
        lheight = rheight = 0
        l = r = 0
        res = []
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                # current point
                cp = [left[l][0], max(left[l][1], rheight)]
                lheight = left[l][1]
                l += 1
            elif left[l][0] > right[r][0]:
                cp = [right[r][0], max(right[r][1], lheight)]
                rheight = right[r][1]
                r += 1
            else:
                cp = [left[l][0], max(left[l][1], right[r][1])]
                lheight = left[l][1]
                rheight = right[r][1]
                l += 1
                r += 1
            if len(res) == 0 or res[-1][1] != cp[1]:
                res.append(cp)
        res.extend(left[l:] or right[r:])
        return res

    def getSkyline(self, buildings):
        import heapq
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, 0) for _, R, _ in buildings}))
        res = [[0, 0]]
        heap = [[0, float("inf")]]
        for x, H, R in events:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if H:
                heapq.heappush(heap, [H, R])
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])
        return res[1:]


a = Solution()
print(a.getSkyline2([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(a.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
