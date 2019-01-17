class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:return 0
        if n <= 3:
            return 1
        res = 1
        s = "122"
        a = "1"
        i = 2
        tmp_n = 3
        while tmp_n <= n:
            # while s[i - 1] == s[i]:
            #     i +=1
            print(tmp_n,n)
            if a == "1":
                res += int(s[i])
            s += a*int(s[i])
            tmp_n += int(s[i])
            a = "2" if a == "1" else "1"
            i +=1
        print(tmp_n,n)
        print(s)
        k = -1
        for _ in range(tmp_n-n):
            if s[k] == "1":
                res -= 1
            k -= 1
        return res
        # return res - s[-(tmp_n-n):].count("1")
a = Solution()
print(a.magicalString(4))
