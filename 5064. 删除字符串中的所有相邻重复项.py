class Solution:
    def removeDuplicates(self, S: str) -> str:
        n = len(S)
        if n <= 1:
            return S
        i = 0
        res = ""
        while i < n:
            if res:
                if res[-1] == S[i]:
                    res = res[:-1]
                else:
                    res += S[i]
                i += 1
            else:
                res += S[i]
                i += 1
        return res

    def removeDuplicates1(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return "".join(stack)


a = Solution()
print(a.removeDuplicates1("abbaca"))
