class Solution:
    def grayCode1(self, n):
        """
        格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
        给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        self.nums = ["0", "1"]
        self.res = []
        self.trace("", n)
        return self.res

    def trace(self, s, n):
        if n == 0:
            self.res.append(int(s, 2))
        else:
            for item in self.nums:
                self.trace(s + item, n - 1)

    def grayCode3(self, n):
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)
        return res

    def grayCode5(self, n):
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | (1 << i))
        return res

    def grayCode6(self, n):
        res = []
        self.num = 0

        def helper(n):
            if n == 0:
                res.append(self.num)
                return
            helper(n - 1)
            self.num ^= (1 << n - 1)
            helper(n - 1)

        helper(n)
        return res

    def grayCode7(self, n):
        num = "0" * n
        res = [0]
        c = 2 ** n
        while len(res) < c:
            if num[-1] == "0":
                num = num[:-1] + "1"
                res.append(int(num, 2))
            else:
                num = num[:-1] + "0"
                res.append(int(num, 2))
            # print(num)

            if len(res) == c:
                break
            idx = num.rfind("1")
            if num[idx - 1] == "0":
                num = num[:idx - 1] + "1" + num[idx:]
            else:
                num = num[:idx - 1] + "0" + num[idx:]
            # print(num)
            res.append(int(num, 2))

        return res

    def grayCode(self, n):
        pass



a = Solution()
print(a.grayCode(10))
