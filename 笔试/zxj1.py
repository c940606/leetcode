def helper1(s: str):
    if "[" not in s:
        return s
    left_p = s.find("[")
    right_p = s.rfind("]")
    res = ""
    i = 0
    while i < left_p:
        if s[i].isdigit():
            break
        i += 1
    res += s[:i] + int(s[i:left_p]) * helper(s[left_p + 1:right_p])
    return res


def helper(s: str) -> str:


print(helper("bcd2[ffhg10[hff]]"))
