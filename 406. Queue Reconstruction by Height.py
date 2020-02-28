from typing import List


class Solution:
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        """:arg
        Input:
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        Output:
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        """
        n = len(people)
        res = [-1] * n
        people.sort()
        # print(people)
        for p in people:
            b = 0
            k = p[1]
            while k:
                if res[b] == -1 or res[b][0] >= p[0]:
                    k -= 1
                b += 1
            # print(b)
            while res[b] != -1:
                b += 1
            res[b] = p
            # print(res)
        return res

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people: return []
        people.sort(key=lambda x: (-x[0], x[1]))
        res = [people[0]]
        for p in people[1:]:
            res.insert(p[1], p)
        return res


a = Solution()
print(a.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
