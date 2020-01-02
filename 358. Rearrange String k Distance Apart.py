class Solution:
    def rearrangeString2(self, s: str, k: int) -> str:
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

    def rearrangeString(self, s: str, k: int) -> str:
        from collections import Counter
        import heapq
        if k <= 1: return s
        c = Counter(s)
        n = len(s)
        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)
        res = ""
        while 1:
            #print(heap)
            tmp = []
            for _ in range(k):
                if not heap:return res if len(res) == n else ""
                num, alp = heapq.heappop(heap)
                num += 1
                res += alp
                if num != 0:
                    tmp.append((num, alp))
            # if len(tmp) < k: break
            for t in tmp:
                heapq.heappush(heap, t)
            if not heap: break
        return res if len(res) == n else ""


a = Solution()
print(a.rearrangeString("a", 0))
print(a.rearrangeString(s="aabbcc", k=3))
print(a.rearrangeString(s="aaabc", k=3))
print(a.rearrangeString(s="aaadbbcc", k=2))
print(a.rearrangeString("abcdabcdabdeac", 4))
