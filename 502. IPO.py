class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        import heapq

        P_C = []
        head = []
        n = len(Profits)
        for p, c in zip(Profits, Capital):
            P_C.append((c, p))
        P_C.sort()
        if P_C[0][0] > W:
            return 0
        i = 0
        while k > 0:
            while i < n and P_C[i][0] <= W:
                heapq.heappush(head,-P_C[i][1])
                i += 1
            if head :
                W -= heapq.heappop(head)
            k -= 1
        return W

    def findMaximizedCapital1(self, k, W, Profits, Capital):
        P_C = []
        for p, c in zip(Profits, Capital):
            P_C.append((p, c))
        P_C.sort()
        while k > 0:
            i = len(P_C) - 1
            while i >= 0 and P_C[i][1] > W:
                i -= 1
            if i == -1:
                break
            W += P_C[i][0]
            P_C.pop(i)
            k -= 1
        return W


a = Solution()
print(a.findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
print(a.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]))
print(a.findMaximizedCapital(10, 0, [1, 2, 3], [0, 1, 2]))
