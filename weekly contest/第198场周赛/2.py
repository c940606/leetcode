from typing import List
import collections



class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        tree = collections.defaultdict(list)
        ans = [1] * n
        visited = set()
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(node):
            # print(node)


            left = {}
            visited.add(node)
            for nxt in tree[node]:

                if nxt not in visited:
                    for k, v in dfs(nxt).items():
                        left.setdefault(k, 0)
                        left[k] += v
            left.setdefault(labels[node], 0)
            left[labels[node]] += 1
            ans[node] = left[labels[node]]

            return left

        dfs(0)
        return ans

a = Solution()
# print(a.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
# print(a.countSubTrees(n = 3, edges = [[0,1],[1,2]], labels = "bbb"))
# print(a.countSubTrees(4,
# # [[0,2],[0,3],[1,2]],
# # "aeed")) # 1 1 2 1
# # print(a.countSubTrees(25,
# # [[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],[2,5],[6,2],[1,6],[11,1],[15,11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]],
# # "hcheiavadwjctaortvpsflssg")) # [2,2,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
print(a.countSubTrees(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"))