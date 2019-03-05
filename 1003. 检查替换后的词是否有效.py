import sys


class Solution:
    def isValid(self, S: str) -> bool:
        sys.setrecursionlimit(1000000)
        n = len(S)
        if n % 3 != 0 or n < 3:
            return False
        flag = set()

        def helper(s):
            if s == S:
                return True
            if s in flag or len(s) > n:
                return False
            for i in range(len(s)):
                if helper(s[:i] + "abc" + s[i:]):
                    return True
                else:
                    flag.add(s[:i] + "abc" + s[i:])
            # print(flag)
            return False

        return helper("abc")

    # def isValid1(self, S: str) -> bool:
    # from collections import deque
    # n = len(S)
    # if n % 3 != 0 or n < 3:
    #     return False
    # dq = deque(S)
    # # print(dq)
    # while dq:
    #     if dq[0] + dq[1] + dq[2] == "abc":
    #         dq.popleft()
    #         dq.popleft()
    #         dq.popleft()
    #     elif dq[-3] + dq[-2] + dq[-1] == "abc":
    #         dq.pop()
    #         dq.pop()
    #         dq.pop()
    #     elif dq[0] + dq[-2] + dq[-1] == "abc":
    #         dq.popleft()
    #         dq.pop()
    #         dq.pop()
    #     elif dq[0]+dq[1]+dq[-1] == "abc":
    #         dq.popleft()
    #         dq.popleft()
    #         dq.pop()
    #     else:
    #         return False
    # return True

    def isValid2(self, S: str) -> bool:
        n = len(S)
        if n % 3 != 0 or n < 3:
            return False
        while S:
            idx = S.find("abc")

            if idx == -1:
                return False
            S = S[:idx] + S[idx + 3:]

        return True

    def isValid3(self, S: str) -> bool:
        stack = []
        for s in S:
            if s == "c":
                if stack[-2:] == ["a", "b"]:
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s)
        return True if not stack else False


a = Solution()
print(a.isValid3("aabcbc"))
print(a.isValid2("abccba"))
print(a.isValid2("cababc"))
print(a.isValid2("abcabcababcc"))
print(a.isValid3(
    "cbbbbcaaaccbaabccabacabcacbabbabbcbacabacabcabbccbccbccbcaccbacaabaaababacbbccabbcbcbabbcbabcacabcbababcaccbcbbbaaabbcbccaaabcbababaaaccbacbbcaabbacbbbabcccacbaacacccbcccbbbbccaaabaaababcbbaacbcccaaabcbacccaacbbbaabababbbbababcbaaaabbcacbacaaabbcacbccbbbbaabcacbccababaaaacbabbbaaccbccaacacccaaabacaaaacacbbaabcabcbcccbcabaaaccbcbaaaccaacbabcaabbccacbbcbbbcaccbaccacaabcbcccacacaccaabbcaaababbbbbbcabcbbacabbbbbaabcbabbbccaabccabccaaaccabcbcbabbcaccabcbaabaaabacccacacabbaccbabbbacaaabacacabacbcabaabaccacbbaacbcaccaccbacbaacbcbabccbcacbbbcabaabaabbabbcbbbcbbaabababcacacacbcabbccbbbacacccbbbbbbcbabaacacbbbaccbcaaccaccabbabbcbaababbcacaababaababcccbbcaaaabccabbbcbbaacacabaabbaabcaabaacaabcbaaabaccbbcbaaababcacaacabcbbbbabaccbabbccacbbbcbacccbbbcabaaaacacaacbbcabbbbaacacababccaaacaccaaaacbabbcacaabaacaaabcacaabcaaaaaaacbbabbababcbbccbabbabaccbbcccacaabcbccacaacbacbcccbabababababbacbabacbcccccbbcbcbabbbbaacbbabacccbcccbcaccabacaacbbbabacccccbcbbbacaccacccbccbbbcbcbaacbbaabaacbacabacacaaaccaaacabbbaabcaacacbaaabcbbbbcaacaaccbbbccbababcbcacbcbcbbaabcacbbcacaacacccababbcacbbcaaccaacbbabccabbccbacacaccccccbcbbcbabcabbcaabbaabaccababcbcbcbabbcabcbabacaababcbcacbaacbcccbbbcbaacabcccbbabccacaaaaccaabccbbaabababcacabbaccbbacbcbcaacabbaccccabbccbbcabcbcccaabcccbabbacabccaacababcaaaacccbabcccabcccabccbacaacabcbbaacbaacbbcbaaaacbbcaccbacaccaaaccabaaabcbabababbcbbcbacbabaacbbbaacabbbaacbaccccaaccccabcabaabaccacaaacabbbbcbccccbcacaacbcbbbcbabcbccaaabbaccbaacccbaacbbbbcccacbcacabccbbcbabbccabbbaabaacbbacacacccbcbcbaabcccacbccbbcacaababbcbaaabaccaaaaacbbbacaaaaabbacaabacbcaccaacbacbaaaabcbaaabcccccbcacbccacbccccaacaaccbbcbabcbaacbbabbbbaabcacbaaacbbcabcbcbbbcabbbbcbcbacccbcaacaccccbcccacbbbbbacbccaabcbabcacacbbaccbbbaccbcaacacabaaccbccabbccbacbaacbbbbacacccabbbbabaaaabcbabcccacccababbabcabbbaabacbcbaaccccacbbbccccacaaaacabaacaccaabccacbbbccaabbccccbccbbbabacbabacbabcbaccbabbaccaccbabcababbbbcbbcabababaacaccacbacccabcacbbbcccacacabcabccaacbacbcaccbaaaacbbccccccaabbabcbaaaacbbbaabbcacabaccabbcbbbbabbccabcccccbbcbbcccbbacacbaaacccccbbcaacaacabbbcacaaaaaacabacbbbbbacbbacbbcbbbcbbaccaacbcbaaaabbbababbbccccaabacbcaacacbbcacccaacccccbbccbbbbbacbabcabbcacccbcbabbaabbacaabaacabcccbbbbcacabbbaacaaacbabbaccaacabbcbbaaabaccaccacccbbbacaccacbabbaacabbcbbcbbccbbbacbbacbbbabcaababaacbaacaabbacbabbccccaccccaabbaaabcccabccbccaaacbbccabbbcbaaaacabbbbbbcbbacbbcccbbabbacbbccbccccccaabacaabaaaccccaabcacbbccbbabccaacccaababbccbabcbabcccbbabaaaababaabbbcbabbccaacbacccaabccababccabcbbcccaacabbbcbaaabbcaacbbbaabaacbbacbbcacbcabccbbccbcbcbbcbaacacbbbbcacbabbaacccaccbacbbcabbbbabcabaabbcaacabbbbbbccbacacaaacabaacbcbacbaaacabcbbcbbbabaccabaaaacaaaaaacaccbccaabaabcaaabaaababcabcccbbcacbcacaabbaaacbbbbcbabaabaabacacaaccbaacabcacbaaabbacccbccaabbaccabbbbacbcbccbcbbcbcbcbcabcccbccaacacccccbbbabbabcbcbabbacaabcbaabbacbcaccacacccacbabbabacababcbaccaabcbacabbacaaaabccbbbbcaabbccbcccccbccacaababcccacbcbcbccabbcbcbcccccccacaaccbbccccbbbcabbacaacacbbabcaacacbcccacbcbcbaaaaccaabaaabcabcaacaacabaacccabaabbaac"))
