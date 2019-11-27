class Solution:
    def isAdditiveNumber1(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return False
        res = []
        n = len(num)

        def helper(idx):
            if idx == n and len(res) > 2:
                return True
            for i in range(idx, n):
                if num[idx] == "0" and i > idx:
                    break
                tmp = int(num[idx:i + 1])
                tmp_n = len(res)
                if tmp_n >= 2 and tmp > res[-1] + res[-2]:
                    break
                if tmp_n <= 1 or tmp == res[-1] + res[-2]:
                    res.append(tmp)
                    if helper(i + 1):
                        return True
                    res.pop()
            return False

        return helper(0)

    def isAdditiveNumber(self, num):
        def isValid(sub1, sub2, num):
            # print(sub1, sub2, num)
            if not num: return True
            sub1, sub2, = sub2, str(int(sub1) + int(sub2))
            return num.startswith(sub2) and isValid(sub1, sub2, num[len(sub2):])

        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == "0" and i > 1: return False
            sub1 = num[:i]
            for j in range(1, n):
                # 剩下的长度都没有前面两个数最大长度长
                if max(i, j) > n - i - j: break
                if num[i] == "0" and j > 1: break
                sub2 = num[i: i + j]
                # 找到两个数, 看后面的数是否能引出来
                if isValid(sub1, sub2, num[i + j:]): return True
        return False


a = Solution()
print(a.isAdditiveNumber("112358"))
print(a.isAdditiveNumber("199100199"))
