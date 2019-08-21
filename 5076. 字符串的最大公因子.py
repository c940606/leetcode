class Solution:
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        res = ""
        i = 0
        j = 0
        while i < len(str1) and j < len(str2) and str1[i] == str2[j]:
            res += str1[i]
            i += 1
            j += 1

        def check(res, tmp):
            # print(res, tmp)
            loc = tmp.find(res)
            while loc != -1:
                if loc == len(tmp) - len(res):
                    return True
                loc = tmp.find(res, loc + len(res))
            return False

        while res:
            if check(res, str1) and check(res, str2):
                return res
            res = res[:-1]

        return res

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #print(str1, str2)
        n1 = len(str1)
        n2 = len(str2)
        if n1 < n2:
            return self.gcdOfStrings(str2, str1)
        elif not str1.startswith(str2):
            return ""
        elif not str2:
            return str1
        else:
            return self.gcdOfStrings(str1[len(str2):], str2)


a = Solution()
print(a.gcdOfStrings(str1="ABCABC", str2="ABC"))
# print(a.gcdOfStrings(str1="ABABAB", str2="ABAB"))
# print(a.gcdOfStrings(str1="LEET", str2="CODE"))
# print(a.gcdOfStrings("asf", ""))
