class Solution:
    def highFive(self, items):
        from collections import defaultdict
        import bisect
        lookup = defaultdict(list)
        for idx, score in items:
            bisect.insort_left(lookup[idx], score)
        # print(lookup)
        res = []
        for i in range(len(lookup)):
            avg = (sum(lookup[i + 1][-5:])) // 5
            res.append([i + 1, avg])
        return res


a = Solution()
print(a.highFive([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
