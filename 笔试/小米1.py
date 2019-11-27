c = int(input())
data = []
# c = 4
# data = [
#     [0, 0, 2, 4],
#     [0, 2, 2, 2],
#     [0, 4, 2, 2],
#     [8, 8, 2, 2]
# ]
for _ in range(c):
    data.append(list(map(int, input().split())))
res = []
for d in data:
    tmp = []
    for i in d:
        if not tmp :
            if i != 0:
                tmp.append(i)
        else:
            if tmp[-1] == i:
                tmp.append(tmp.pop() * 2)
            else:
                tmp.append(i)
    tmp = tmp + (len(d) - len(tmp)) * [0]
    res.append(tmp)
for t in res:
    print(" ".join(map(str, t)))
