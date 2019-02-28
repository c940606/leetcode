from collections import deque


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # 建图
        from collections import defaultdict
        import  heapq
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1],time[2]))
        res = {}
        queue =[(0,K)]
        while queue:
            time,node = heapq.heappop(queue)
            if node not in res:
                res[node] = time
                for v,w in graph[node]:
                    heapq.heappush(queue,(time+w,v))
        return max(res.values()) if len(res) == N else -1

    def networkDelayTime1(self, times, N, K):
        from collections import defaultdict
        graph = defaultdict(lambda :[float("inf")]*(N+1))
        for i in range(N):
            graph[i+1][i+1] = 0
        for u,v,t in times:
            graph[u][v] = t
        res = [float("inf")] * (N+1)
        res[K] = 0
        visited = set()
        for _ in range(N):
            cur_min = float("inf")
            idx = None
            for i in range(1,N+1):
                if i not in visited and cur_min > res[i]:
                    cur_min = res[i]
                    idx = i
            if idx == None:
                return -1
            visited.add(idx)
            for i in range(1,N+1):
                if i not in visited:
                    res[i] = min(res[i],graph[idx][i]+cur_min)
        return max(res[1:])




a = Solution()
print(a.networkDelayTime1([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
