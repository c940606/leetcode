class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])

        # 深度遍历(DFS)
        def dfs(start, end, visited):
            # 当图中有此边,直接输出
            if (start, end) in weight:
                return weight[(start, end)]
            # 图中没有这个点
            if start not in graph or end not in graph:
                return 0
            # 已经访问过
            if start in visited:
                return 0
            visited.add(start)
            res = 0
            for tmp in graph[start]:
                res = (dfs(tmp, end, visited) * weight[(start, tmp)])
                # 只要遍历到有一个不是0的解就跳出
                if res != 0:
                    # 添加此边,以后访问节省时间
                    weight[(start, end)] = res
                    break
            # vistied.remove(start)
            return res

        res = []
        for que in queries:
            # 用集合记录是否已经访问节点
            tmp = dfs(que[0], que[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res

    def calcEquation1(self, equations, values, queries):
        from collections import defaultdict, deque
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])
        res = []
        for start, end in queries:
            if (start, end) in weight:
                res.append(weight[(start, end)])
                continue
            if start not in graph or end not in graph:
                res.append(-1)
                continue
            if start == end:
                res.append(1.0)
                continue
            stack = deque()
            # 将从start点可以到达下一个节点压入栈内
            for tmp in graph[start]:
                stack.appendleft((tmp, weight[(start, tmp)]))
            # 记录访问节点
            visited = {start}
            # 为了跳出双循环
            flag = False
            while stack:
                c, w = stack.pop()
                if c == end:
                    flag = True
                    res.append(w)
                    break
                visited.add(c)
                for n in graph[c]:
                    if n not in visited:
                        weight[(start, n)] = w * weight[(c, n)]
                        stack.appendleft((n, w * weight[(c, n)]))
            if flag:
                continue
            res.append(-1.0)
        return res


a = Solution()
print(
    a.calcEquation1([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print(a.calcEquation1([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
                      , [3.0, 4.0, 5.0, 6.0]
                      , [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]))
