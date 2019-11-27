def calculateMaxOil(numNodes, sourceNode, newwork):
    from collections import defaultdict
    graph = defaultdict(list)
    weights = defaultdict(int)
    # 建图
    for x, y, w in newwork:
        graph[x].append(y)
        graph[y].append(x)
        weights[tuple(sorted([x, y]))] = w
    res = 0

    def dfs(sourceNode, min_num, tmp):
        nonlocal res
        for nxt_node in graph[sourceNode]:
            w = weights[tuple(sorted([sourceNode, nxt_node]))]
            if min_num > w:
                dfs(nxt_node, min(min_num, w), tmp + w)
        res += tmp

    dfs(sourceNode, float("inf"), 0)
    return res
