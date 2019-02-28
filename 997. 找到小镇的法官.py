class Solution:
    def findJudge(self, N: 'int', trust: 'List[List[int]]') -> 'int':
        from collections import defaultdict
        lookup = defaultdict(set)
        for i,j in trust:
            lookup[i].add(j)
        # print(lookup)
        # person = []
        # flag = set(lookup.keys())
        # for p in range(1,N+1):
        #     if p not in flag:
        #         person.append(p)
        # print(person)
        # if not person :
        #     return -1
        # person = person[0]
        # # print(lookup)
        # for j in range(1,N+1):
        #     if j == person:
        #         continue
        #     if person not in lookup[j]:
        #         return -1
        # return person
        if len(lookup.keys()) != N-1:
            return -1

        res = {i for i in range(1,N+1)}
        for tmp in lookup.values():
            res &= tmp
        return res.pop() if res else -1

    def findJudge1(self, N: 'int', trust: 'List[List[int]]') -> 'int':
        degree = [0]*(N+1)
        for i,j in trust:
            degree[i] -= 1
            degree[j] += 1
        for k in range(1,N+1):
            if degree[k] == N-1:
                return k
        return -1
a  = Solution()
print(a.findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]))
print(a.findJudge(N = 3, trust = [[1,2],[2,3]]))
print(a.findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(a.findJudge(N = 2, trust = [[1,2]]))
print(a.findJudge(N = 3, trust = [[1,3],[2,3]]))