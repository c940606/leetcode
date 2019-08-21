class Solution:
    def permute(self, S: str):
        res = [""]
        i = 0
        n = len(S)
        while i < n:
            if S[i] == "{":
                idx = S.find("}", i + 1)
                # print(idx)
                tmp = S[i + 1:idx].split(",")
                i = idx + 1
                next_time = []
                for item in res:
                    for a in tmp:
                        next_time.append(item + a)
                res = next_time
            else:
                for k in range(len(res)):
                    res[k] += S[i]
                i += 1
        return sorted(res)


a = Solution()
print(a.permute("{a,b}c{d,e}f"))
print(a.permute("abcd"))
print(a.permute("{a,b}{z,x,y}"))
