import itertools


class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，
        得到一个字符串S。返回所有可能的原始字符串到一个列表中。
        原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。
        此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。
        最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        res = []

        def f(S):
            if not S or (len(S) > 1 and S[0] == "0" and S[-1] == "0"):
                return []
            if S == "0":
                return [S[0]]
            if S[0] == "0" and len(S) > 1:
                return [S[0]+ "." + S[1:]]
            if S[-1] =="0" and len(S)  > 1:
                return [S]
            return [S] +  [S[:i] + "." + S[i:] for i in range(1, len(S))]

        for i in range(1,len(S)):
            for x,y in itertools.product(f(S[:i]), f(S[i:])):
                res.append("(%s, %s)"%(x,y))
        return res

    def ambiguousCoordinates1(self, S):
        S = S[1:-1]
        n = len(S)
        res = []
        def helper(S):
            tmp_n = len(S)
            tmp = []
            if S == "0":
                return [0]
            # if
            #
            # for j in range(tmp_n):

        for i in range(1,n-1):
            for front in helper(S[:i]):
                for last in helper(S[i:]):
                    pass

a = Solution()
print(a.ambiguousCoordinates("(123)"))
print(a.ambiguousCoordinates("(0123)"))
print(a.ambiguousCoordinates("(100)"))
