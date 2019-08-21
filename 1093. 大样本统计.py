class Solution:
    def sampleStats(self, count):

        res = [0.0] * 5

        lookup = []
        for idx, val in enumerate(count):
            if val != 0:
                lookup.append([idx, val])
        #print(lookup)
        num = 0
        s = 0
        for idx, val in lookup:
            num += val
            s += idx * val
        if num % 2 == 0:
            l = num // 2
            t = 0


            for i,item in enumerate(lookup):
                idx = item[0]
                val = item[1]
                t += val
                #print(t)
                if t > l :
                    res[3] = idx
                    break
                if t == l:
                    #print("fdaf")
                    res[3] = (idx + lookup[i+1][0]) / 2
                    break
        else:
            l = num // 2
            t = 0
            for i,item in enumerate(lookup):
                idx = item[0]
                val = item[1]
                t += val
                #print(t)
                if t >= l :
                    res[3] = idx
                    break

        lookup = sorted(lookup, key=lambda x:x[1])
        res[-1] = float(lookup[-1][0])

        res[0] = float(lookup[0][0])
        res[1] = float(lookup[-1][0])
        res[2]  = float(s/ num)

        return res


a = Solution()
print(a.sampleStats(
    [0, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
