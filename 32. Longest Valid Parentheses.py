class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        res.sort()
        # print(res)
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans

    def longestValidParentheses1(self, s: str) -> int:

        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):

            if i > 0 and s[i] == ")":
                if i > 0 and s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
                print(dp)
        return res


a = Solution()
# print(a.longestValidParentheses1(")(()())"))
# print(a.longestValidParentheses1("(()"))
# print(a.longestValidParentheses1(")()())"))
# print(a.longestValidParentheses1("()(())"))
print(a.longestValidParentheses1("(()))())("))