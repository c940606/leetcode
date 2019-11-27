class Solution:
    def countDigitOne(self, n: int) -> int:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[-1] + str(i).count("1"))
        print(",".join(map(str, res)))

        # return res
    def countDigitOne1(self, x: int) -> int:
        return x//((1-x)*(1-x)**10) + ((1-x**10)//(1-x))**2*g(x**10)


if __name__ == '__main__':
    a = Solution()
    a.countDigitOne(1000)
    # g(x) = x/((1-x)*(1-x)^10) + ((1-x^10)/(1-x))^2*g(x^10)
    print()
