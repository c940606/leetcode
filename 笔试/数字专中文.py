def numToChina(nums):
    single_digit = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]

    # tens = ["拾", "佰", "仟", "万", "亿"]

    def helper(nums):
        # print(nums)
        if nums < 10:
            return single_digit[nums:nums + 1]
        for p, c in enumerate(["拾", "佰", "仟", "万", ], 1):
            if nums < 10 ** (p + 1):
                return helper(nums // (10 ** p)) + [c] + helper(nums % (10 ** p))
        if nums < 100000000:
            return helper(nums // 100000000) + ["亿"] + helper(nums % 100000000)

    return "".join(helper(nums))


print(numToChina(10))
print(numToChina(1234))
print(numToChina(10010))
