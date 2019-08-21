class Solution:
    def fractionToDecimal1(self, numerator: int, denominator: int) -> str:
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

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = []
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        # 无小数
        if b == 0:
            return "".join(res)
        res.append(".")
        # 处理余数
        # 把所有出现过的余数记录下来
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            loc[b] = len(res)
        return "".join(res)


a = Solution()
print(a.fractionToDecimal(8, 4))
print(a.fractionToDecimal(2, 3))
print(a.fractionToDecimal(5, 6))
print(a.fractionToDecimal(9, 10))
print(a.fractionToDecimal(-50, 8))
print(a.fractionToDecimal(7, -12))
