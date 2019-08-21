class Solution:
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        import functools
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        @functools.lru_cache(None)
        def helper(i, j, k):
            if i == n1 and j == n2 and k == n3:
                return True

            if i < n1 and j < n2 and k < n3 and s1[i] == s2[j] == s3[k]:
                if helper(i + 1, j, k + 1) or helper(i, j + 1, k + 1):
                    return True
            elif i < n1 and k < n3 and s1[i] == s3[k]:
                if helper(i + 1, j, k + 1):
                    return True
            elif j < n2 and k < n3 and s2[j] == s3[k]:
                if helper(i, j + 1, k + 1):
                    return True
            return False

        return helper(0, 0, 0)

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3: return False

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        dp[0][0] = True
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = (dp[0][j - 1] and s2[j - 1] == s3[j - 1])

        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        # print(dp)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        # print(dp)
        return dp[-1][-1]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from collections import deque
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3: return False

        queue = deque()
        queue.appendleft((0, 0))
        visited = set()
        while queue:
            i, j = queue.pop()
            if i == n1 and j == n2:
                return True
            if i < n1 and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                queue.appendleft((i + 1, j))
            if j < n2 and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                queue.appendleft((i, j + 1))

        return False


a = Solution()
print(a.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
# print(a.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
# print(a.isInterleave(
#     "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
#     , "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
#     ,
#     "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
