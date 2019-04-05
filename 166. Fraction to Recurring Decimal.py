class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        trading = numerator // denominator
        res.append(str(trading))
        num = numerator % denominator
        if num == 0: return "".join(res)
        res.append(".")
        lookup = {num: len(res)}
        while num != 0:
            num *= 10
            res.append(str(num // denominator))
            num %= denominator
            if num in lookup:
                idx = lookup[num]
                res.insert(idx, "(")
                res.append(")")
                break
            else:
                lookup[num] = len(res)
        # print(res)
        return "".join(res)


a = Solution()
print(a.fractionToDecimal(2, 3))
print(a.fractionToDecimal(5, 6))
print(a.fractionToDecimal(9, 10))
