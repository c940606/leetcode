class Solution:
    def camelMatch(self, queries, pattern):
        res = []
        n = len(pattern)
        if not queries:
            return res

        def helper(q):
            i = 0
            j = 0
            while i < n and j < len(q):
                # query 和 patter 字母相等
                if pattern[i] == q[j]:
                    i += 1
                    j += 1
                else:
                    # 如果是大写 直接False
                    if q[j].isupper():
                        return False
                    # 小写,j 向后移
                    j += 1
            # query 没遍历完,看是否还有大写字母
            while j < len(q):
                if q[j].isupper():
                    return False
                j += 1
            return True if i == n else False

        for query in queries:
            if helper(query):
                res.append(True)
            else:
                res.append(False)
        return res

    def camelMatch1(self, queries, pattern):

        res = []

        def helper(query):
            j = 0
            for q in query:
                if j < len(pattern) and q == pattern[j]:
                    j += 1
                elif q.isupper():
                    return False
            return True if j == len(pattern) else False

        for query in queries:
            if helper(query):
                res.append(True)
            else:
                res.append(False)
        return res

    def camelMatch2(self, queries, pattern):

        def find_upper(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t)
            return all(c in it for c in s)

        return [find_upper(q) == find_upper(pattern) and issup(pattern, q) for q in queries]


a = Solution()
print(a.camelMatch2(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB"))
print(a.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa"))
print(a.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBaT"))
