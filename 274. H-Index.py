class Solution:
    def hIndex1(self, citations) -> int:
        if not citations:
            return 0
        n = len(citations)
        bucket = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                bucket[n] += 1
            else:
                bucket[citation] += 1
        print(bucket)
        cur_sum = 0
        idx = n
        for num in bucket[::-1]:
            cur_sum += num
            if cur_sum >= idx:
                return idx
            idx -= 1
        return 0

    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        #n = len(citations)
        #print(citations)
        for i, citation in enumerate(citations):
            if citation <= i:
                return i
        return len(citations)


a = Solution()
print(a.hIndex([3, 0, 6, 1, 5]))
print(a.hIndex([100]))
