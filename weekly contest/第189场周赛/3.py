from typing import List
import collections

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        cf = [set(tmp) for tmp in favoriteCompanies]

        n = len(cf)
        res = []
        for i in range(n):
            flag = False
            for j in range(n):
                if i == j: continue
                if len(cf[i]) <= len(cf[j]) and cf[i].issubset(cf[j]):
                    flag = True
                    break
            if not flag:
                res.append(i)
        return res
a = Solution()
print(a.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
print(a.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print(a.peopleIndexes(favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]))
                

