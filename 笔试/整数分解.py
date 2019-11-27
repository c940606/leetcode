num = int(input())

res = []

def dfs(num, tmp):
    if num == 0 :
        res.append("+".join(tmp))
        return
    for i in range(1, num + 1):
        if tmp and (1 + int(tmp[-1])) * int(tmp[-1]) // 2 > num:
            break
        dfs(num - i, tmp + [str(i)])


dfs(num, [])
for t in res:
    print(t)
