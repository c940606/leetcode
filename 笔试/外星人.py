from collections import defaultdict
import sys

if __name__ == '__main__':
    #words = ["wrt", "wrf", "er", "ett", "rftt"]
    words = ["cd", "bd", "d"]
    # 建图
    graph = defaultdict(list)
    indegree = defaultdict(int)
    all_alp = set()
    all_alp.update(set(words[0]))
    for i in range(1, len(words)):
        all_alp.update(set(words[i]))
        for a, b in zip(words[i - 1], words[i]):
            if a != b:
                graph[a].append(b)
                indegree[b] += 1
                break
    # 拓扑排序, 找到入度为0, 当有两个入度为0 说明不能排序
    bfs = []
    # 找到入度为0的子母
    for alp in all_alp:
        if indegree[alp] == 0:
            bfs.append(alp)
            if len(bfs) >= 2:
                print("invaild")
                sys.exit()
    res = ""
    while bfs:
        next_bfs = []
        for b in graph[bfs[0]]:
            indegree[b] -= 1
            if indegree[b] == 0:
                next_bfs.append(b)
            if len(next_bfs) >= 2:
                print("invaild")
                sys.exit()
        res += bfs[0]
        bfs = next_bfs
    #print(res)
    if len(res) != len(all_alp):
        print("invaild")
        sys.exit()
    print(res)




