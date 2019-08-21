class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        from collections import Counter
        n = len(s)
        cur = 1
        i = 0
        res = [0] * n
        lookup = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        print(lookup)
        for key, v in lookup:
            # print(key,v)
            for _ in range(v):

                res[i] = key
                if i > 0 and res[i] == res[i - 1]:
                    # print(res)
                    return ""
                if i >= k and key in res[i - k + 1:i]:
                    print(res)
                    return ""
                i += k
                if i >= n:
                    i = cur
                    cur += 1
        # print(res)
        return "".join(res)

    def rearrangeString1(self, s: str, k: int) -> str:
        from collections import Counter
        import heapq
        if k == 0 or k == 1: return s
        heap = []
        for a, b in Counter(s).items():
            heapq.heappush(heap, (-b, a))
        res = ""
        while heap:
            tmp = []
            for _ in range(k):
                if not heap:
                    if len(res) == len(s):
                        return res
                    else:
                        return ""
                b, a = heapq.heappop(heap)
                res += a
                tmp.append((b + 1, a))
            for b, a in tmp:
                if b != 0:
                    heapq.heappush(heap, (b, a))
        return res


a = Solution()
# print(a.rearrangeString1(s="aabbcc", k=3))
# print(a.rearrangeString1(s="aaabc", k=3))
print(a.rearrangeString1(s="aaadbbcc", k=2))
# print(a.rearrangeString1("abcdabcdabdeac", 4))
