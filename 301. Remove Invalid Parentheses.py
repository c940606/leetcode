class Solution:
    def removeInvalidParentheses1(self, s: str):

        # 找字符串最长有效括号的长度
        def longestVaildParentheses(s: str):
            res = 0
            stack = []
            for a in s:
                if a == "(":
                    stack.append("(")
                elif a == ")":
                    if stack:
                        res += 2
                        stack.pop()
            return res

        def helper(s, left_p, right_p, open, tmp):
            # 当都小于0 都不满足条件
            if left_p < 0 or right_p < 0 or open < 0:
                return
            # s剩余的括号都不够组成的
            if s.count("(") < left_p or s.count(")") < right_p:
                return
            if not s:
                # 输出
                if left_p == 0 and right_p == 0 and open == 0:
                    res.add(tmp)
                return
            if s[0] == "(":
                # 用 (
                helper(s[1:], left_p - 1, right_p, open + 1, tmp + "(")
                # 不用 (
                helper(s[1:], left_p, right_p, open, tmp)
            elif s[0] == ")":
                # 用 )
                helper(s[1:], left_p, right_p - 1, open - 1, tmp + ")")
                # 不用 (
                helper(s[1:], left_p, right_p, open, tmp)
            else:
                helper(s[1:], left_p, right_p, open, tmp + s[0])

        l = longestVaildParentheses(s)
        res = set()
        # 因为l是最长的, 所以左括号和右括号各一半, 再用open表示左右括号抵消多少
        helper(s, l // 2, l // 2, 0, "")
        return list(res)

    def removeInvalidParentheses2(self, s: str):
        from collections import deque
        res = set()
        # 删除左括号的个数
        rmL = 0
        # 删除右括号的个数
        rmR = 0
        for a in s:
            if a == "(":
                rmL += 1
            elif a == ")":
                if rmL != 0:
                    rmL -= 1
                else:
                    rmR += 1
        # 是否满足有效括号
        def isValid(s):
            cnt = 0
            for a in s:
                if a == "(":
                    cnt += 1
                elif a == ")":
                    cnt -= 1
                    if cnt < 0: return False
            return True
        # 记录此时 s , 左右括号的个数
        queue = deque([(s, rmL, rmR)])
        visited = set()
        visited.add((s, rmL, rmR))
        while queue:
            tmp_s, left_p, right_p = queue.pop()
            # 输出条件
            if left_p == 0 and right_p == 0 and isValid(tmp_s):
                res.add(tmp_s)
            for i in range(len(tmp_s)):
                # 为字母时候
                if tmp_s[i] not in "()": continue
                if tmp_s[i] == "(" and left_p > 0:
                    t = tmp_s[:i] + tmp_s[i + 1:]
                    if (t, left_p - 1, right_p) not in visited:
                        queue.appendleft((t, left_p - 1, right_p))
                        visited.add((t, left_p - 1, right_p))
                if tmp_s[i] == ")" and right_p > 0:
                    t = tmp_s[:i] + tmp_s[i + 1:]
                    if (t, left_p, right_p - 1) not in visited:
                        queue.appendleft((t, left_p, right_p - 1))
                        visited.add((t, left_p, right_p - 1))
        return list(res)

    def removeInvalidParentheses(self, s: str):
        res = []

        def remove(s, ibegin, jbegin, tmp1, tmp2):
            # print(s, ibegin, jbegin, tmp1, tmp2)
            left_p = 0
            right_p = 0
            for i in range(ibegin, len(s)):
                if s[i] == tmp1: left_p += 1
                if s[i] == tmp2: right_p += 1
                if left_p < right_p:
                    for j in range(jbegin, i + 1):
                        if s[j] == tmp2 and (j == jbegin or s[j - 1] != tmp2):
                            remove(s[:j] + s[j + 1:], i, j, tmp1, tmp2)

                    return
            print(s)
            rev = s[::-1]
            if tmp1 == "(":
                remove(rev, 0, 0, ")", "(")
            else:
                res.append(rev)

        remove(s, 0, 0, "(", ")")
        return res


a = Solution()
# print(a.removeInvalidParentheses("(a)())()"))
# print(a.removeInvalidParentheses("()())()"))
# print(a.removeInvalidParentheses(""))
# print(a.removeInvalidParentheses(")("))
# print(a.removeInvalidParentheses("nasdf)dfa"))
# print(a.removeInvalidParentheses("(()y"))
# print(a.removeInvalidParentheses("x("))
# print(a.removeInvalidParentheses(")()("))
# print(a.removeInvalidParentheses(""))
# print(a.removeInvalidParentheses("(((k()(("))
# print(a.removeInvalidParentheses("())((d)))()(()))(())"))
print(a.removeInvalidParentheses("))()"))
