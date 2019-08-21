class Solution:
    def restoreIpAddresses1(self, s):
        """
        给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
        ---
        输入: "25525511135"
        输出: ["255.255.11.135", "255.255.111.35"]
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        if len(s) > 15:
            return []
        self.dps("", s, 3)
        return self.res

    def dps(self, temp, s, n):
        # print(temp)

        # if temp and int(temp.split(".")[-2])>255:
        # 	# print(temp.split(".")[-2])
        # 	return

        if not s:
            return
        if n == 0:
            # print(temp+s)
            split_s = (temp + s).split(".")
            for item in split_s:
                if len(item) > 1 and item[0] == "0":
                    return
            if max(map(int, split_s)) <= 255:
                self.res.append(temp + s)
            # return
        #
        # if temp[:-1] > "255":
        # 	return

        for i in range(0, len(s)):
            # print(temp+s[0:i+1])
            # if temp.split(".")[-1] > "255":
            # 	break

            self.dps(temp + s[0:i + 1] + ".", s[i + 1:], n - 1)
            # temp += "."

    def restoreIpAddresses2(self, s):
        res = []

        def helper(s, tmp, k):
            if not s and k == 0:
                res.append(".".join(tmp))
                return

            for i in range(len(s)):
                if (len(s[:i + 1]) > 1 and s[0] == "0") or len(s) > k * 3:
                    break
                if 0 <= int(s[:i + 1]) <= 255:
                    helper(s[i + 1:], tmp + [s[:i + 1]], k - 1)
                else:
                    break

        helper(s, [], 4)
        return res

    def restoreIpAddresses3(self, s):
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                # print(j)
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

    def restoreIpAddresses(self, s):
        n = len(s)
        res = []

        def helper(tmp):
            if not tmp or (tmp[0] == "0" and len(tmp) > 1) or int(tmp) > 255:
                return False
            return True

        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        # print(tmp1, tmp2, tmp3, tmp4)

                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res


a = Solution()
# "010010"
print(a.restoreIpAddresses("010010"))
print(a.restoreIpAddresses("25525511135"))
