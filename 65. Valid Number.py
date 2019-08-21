class Solution:
    def isNumber(self, s: str):
        s = s.strip()
        print(s)
        dot_seen = False
        e_seen = False
        num_seen = False
        for i, a in enumerate(s):
            if a.isdigit():
                num_seen = True
            elif a == ".":
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            elif a == "e":
                if e_seen or not num_seen:
                    return False
                num_seen = False
                e_seen = True
            elif a in "+-":
                if i > 0 and s[i - 1] != "e":
                    return False
            else:
                return False
        return num_seen

    def isNumber1(self, s: str):
        state = [
            {},
            # 状态1,初始状态(扫描通过的空格)
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            # 状态2,发现符号位(后面跟数字或者小数点)
            {"digit": 3, ".": 4},
            # 状态3,数字(一直循环到非数字)
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            # 状态4,小数点(后面只有紧接数字)
            {"digit": 5},
            # 状态5,小数点之后(后面只能为数字,e,或者以空格结束)
            {"digit": 5, "e": 6, "blank": 9},
            # 状态6,发现e(后面只能符号位, 和数字)
            {"sign": 7, "digit": 8},
            # 状态7,e之后(只能为数字)
            {"digit": 8},
            # 状态8,e之后的数字后面(只能为数字或者以空格结束)
            {"digit": 8, "blank": 9},
            # 状态9, 终止状态 (如果发现非空,就失败)
            {"blank": 9}
        ]
        cur_state = 1
        for c in s:
            if c.isdigit():
                c = "digit"
            elif c in " ":
                c = "blank"
            elif c in "+-":
                c = "sign"
            if c not in state[cur_state]:
                return False
            cur_state = state[cur_state][c]
        if cur_state not in [3, 5, 8, 9]:
            return False
        return True

    def isNumber2(self, s: str):
        import re
        return re.compile("[-+]?(\\d+\\.?|\\.\\d+)\\d*(e[-+]?\\d+)?").match(s.strip())
        #return re.match("[-+]?(\\d+\\.?|\\.\\d+)\\d*(e[-+]?\\d+)?", s.strip())


a = Solution()
print(a.isNumber2(" 6 e-1"))
# print(a.isNumber("-+3"))
# print(a.isNumber(" 0.1 "))
# print(a.isNumber(" -90e3   "))
# print(a.isNumber("53.5e93"))
# print(a.isNumber("95a54e53"))
# print(a.isNumber(".."))
# print(a.isNumber("e"))
# print(a.isNumber("."))
# print(a.isNumber(" "))
# print(a.isNumber(". 1"))
# print(a.isNumber(" 1 3 "))
# print(a.isNumber("1 "))
# print(a.isNumber(".-4"))
# print(a.isNumber("+.8"))
# print(a.isNumber(".e1"))
