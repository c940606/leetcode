class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        s = s.split("e")
        n = len(s)

        def helper(t):
            n = len(t)
            i = 0
            while i < n and t[i] == " ":
                i += 1
            if i == n:
                return False
            if i < n and t[i] in ["+", "-"]:
                i += 1
            if i == n:
                return False
            while i < n:
                if t[i] == " ":
                    i += 1
                    continue
                elif not t[i].isdigit():
                    return False
                i += 1
            return True

        print(s, len(s))
        if n == 1:
            num1 = s[0]
            num1 = str(num1).strip()
            # print(num1,len(num1))
            if " " in num1:
                return False

            if num1.count(".") > 1:
                return False
            if "." in num1:
                tmp1, tmp2 = num1.split(".")
                if tmp2 and tmp2[0] in ["+", "-"]:
                    return False
                if tmp1 in ["+","-"] and helper(tmp2):
                    return True
                if tmp1 and tmp1[-1] == " ":
                    return False
                tmp1.strip(" ")
                tmp2.strip(" ")
                # print(bool(tmp1),bool(tmp2))
                if not tmp1 and not tmp2:
                    return False
                if not tmp1 and helper(tmp2):
                    return True
                if not tmp2 and helper(tmp1):
                    return True
                # if len(set(tmp1)) == 1 and tmp1[0]
                if not helper(tmp1) or not helper(tmp2):
                    return False
            else:
                if not helper(num1):
                    return False

        elif n == 2:
            num1 = s[0]
            num2 = s[1]
            if not num1 or not num2:
                return False
            if "." in num2 or not helper(num2):
                return False
            if num1.count(".") > 1:
                return False
            if "." in num1:
                tmp1, tmp2 = num1.split(".")
                if tmp2 and tmp2[0] in ["+", "-"]:
                    return False
                if tmp1[-1] == " " or tmp2[0] == " ":
                    return False
                if tmp1 in ["+","-"] and helper(tmp2):
                    return True
                tmp1.strip(" ")
                tmp2.strip(" ")
                # print(bool(tmp1),bool(tmp2))
                if not tmp1 and not tmp2:
                    return False
                if not tmp1 and helper(tmp2):
                    return True
                if not tmp2 and helper(tmp1):
                    return True
                if not helper(tmp1) or not helper(tmp2):
                    return False
            else:
                if not helper(num1):
                    # print("df")
                    return False

        else:

            return False
        return True


a = Solution()
# print(a.isNumber(" 6 e-1"))
# print(a.isNumber("-+3"))
# print(a.isNumber(" 0.1 "))
# print(a.isNumber(" -90e3   "))
# print(a.isNumber("53.5e93"))
# print(a.isNumber("95a54e53" ))
# print(a.isNumber(".."))
# print(a.isNumber("e"))
# print(a.isNumber("."))
# print(a.isNumber(" "))
# print(a.isNumber(". 1"))
# print(a.isNumber(" 1 3 "))
# print(a.isNumber("1 "))
# print(a.isNumber(".-4"))
# print(a.isNumber("+.8"))
print(a.isNumber(".e1"))
