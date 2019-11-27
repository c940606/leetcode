# n, m, q = map(int, input().split())
# data = input().split()
n, m, q = 4, 10, 6
data = [">", "2", "2", "<"]

def helper(tmp):
    i = 0
    toword = 1
    res = 0
    while 0 <= i < len(tmp):
        if tmp[i] == "<":
            while i - 1 >= 0 and tmp[i - 1] in {"<", ">"}:
                tmp.pop(i)
                i -= 1
            if tmp[i] == "<":
                toword = -1
            else:
                toword = 1
            i += toword

        elif tmp[i] == ">":
            while i + 1 < len(tmp) and tmp[i + 1] in {"<", ">"}:
                tmp.pop(i)
            if tmp[i] == "<":
                toword = -1
            else:
                toword = 1
            i += toword
        else:
            res += int(tmp[i])
            tmp[i] = str(int(tmp[i]) - 1)
            if tmp[i] == "0":
                if toword == 1:
                    tmp.pop(i)
                else:
                    tmp.pop(i)
                    i -= 1
                continue
            i += toword
    return res


for _ in range(q):
    l, r = map(int, input().split())
    tmp = data[l-1: r ]
    print(helper(tmp))

