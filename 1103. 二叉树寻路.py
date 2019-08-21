class Solution:
    def pathInZigZagTree(self, label: int):
        rou = []
        i = 0
        while True:
            tmp = list(range(int(2 ** i), int(2 ** (i + 1) )))
            #print(tmp)
            if i % 2 == 0:
                rou.append(tmp)
            else:
                rou.append(tmp[::-1])
            if tmp[-1] >= label:
                break

            i += 1
            #print(tmp)
            #break
        #print(rou)
        res = []
        n = len(rou) - 1
        loc = rou[n].index(label)
        while n > 0:
            res.insert(0, rou[n][loc])
            n -= 1
            loc //= 2
        #print(res)
        return [1] + res

a = Solution()
print(a.pathInZigZagTree(14))
print(a.pathInZigZagTree(26))
