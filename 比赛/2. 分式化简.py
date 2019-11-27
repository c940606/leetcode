class Solution:
    def fraction(self, cont):
        # if not cont:
        n = len(cont)
        if n == 0: return [0, 0]
        if n == 1:
            return [cont[0], 1]
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        def helper(x1, x2, y1, y2):
            return [x1 * y1 + y2, y1 * x2]

        y = cont.pop()
        x = cont.pop()
        #print(x, y)
        res = helper(x, 1, y, 1)
        #print(res)
        cont.append(res)
        while len(cont) > 1:
            #print(cont)
            y1, y2 = cont.pop()
            x1 = cont.pop()
            res = helper(x1, 1, y1, y2)
            cont.append(res)
        a, b = cont.pop()
        g = gcd(a, b)
        return [a // g, b // g]


a = Solution()
print(a.fraction([3, 2, 0, 2]))
print(a.fraction([0, 0, 3]))
print(a.fraction([1, 1]))
