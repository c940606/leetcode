class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        from itertools import groupby
        # 结果
        res = 0
        n = len(s)
        add_len = 0
        delete_len = 0
        if n < 6:
            add_len = 6 - n
        if n > 20:
            delete_len = n - 20
        # 至少等于这个结果
        res += delete_len + add_len
        # 判读是否数字 小写字母 大写字母 对于重复数字需要几次操作(插入或者删除)
        is_digit = False
        is_lower = False
        is_upper = False
        repeat = 0
        # s取反, 因为对于大于20长度,如何最后部分是重复的, 我们通过删除既能减少个数又能减少重复的
        for k, v in groupby(s[::-1]):
            if k.isdigit(): is_digit = True
            if k.islower(): is_lower = True
            if k.isupper(): is_upper = True
            tmp = len(list(v))
            # 对于重复大于3的, 当和3余数为0, 删除一个即可, 当和3余数为1, 删除2个即可...就能 (这地方要理解一下)
            while delete_len > 0 and tmp >= 3:
                if tmp % 3 == 0:
                    tmp -= 1
                    delete_len -= 1
                elif tmp % 3 == 1 and delete_len >= 2:
                    tmp -= 2
                    delete_len -= 2
                elif tmp % 3 == 2 and delete_len >= 3:
                    tmp -= 3
                    delete_len -= 3
                else:
                    break
            repeat += tmp // 3
        # 看还需要几个操作添加 数字, 大写字母
        cond = 3 - (is_digit + is_lower + is_upper)

        # 添加
        if add_len >= cond:
            cond = 0
        else:
            cond -= add_len
        # 插入使重复数字之间
        if add_len >= repeat:
            repeat = 0
        else:
            repeat -= add_len
        # if repeat > 0:
        res += repeat
        # 将重复数字归0
        if repeat >= cond:
            cond = 0
        else:
            cond -= repeat
        return res + cond


a = Solution()
# print(a.strongPasswordChecker(""))
# print(a.strongPasswordChecker("AAAAAABBBBBB123456789a"))
# print(a.strongPasswordChecker("addd"))
# print(a.strongPasswordChecker("ABABABABABABABABABAB1"))
# print(a.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa"))
# print(a.strongPasswordChecker("..................!!!"))
# print(a.strongPasswordChecker("..."))
print(a.strongPasswordChecker("aaaaaaaAAAAAA6666bbbbaaaaaaABBC"))
