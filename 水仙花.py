res = []
def helper(n, tmp):
    global res
    if n == 0:
        if "".join(map(str, tmp)) == str(sum(t ** len(tmp) for t in tmp)):
            res.append(int("".join(map(str, tmp))))
        return 
    for i in range(10):
        helper(n - 1, tmp + [i])
helper(7, [])
print(res)
