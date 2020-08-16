res = []
with open("input.txt", "r", encoding="utf-8") as f:
    a = f.readline()
    M = int(a)
    res.append(M)
    num = f.readline()
    while num:
        res.append([])
        for _ in range(int(num)):
            b = f.readline()
            res[-1].append(int(b.split()[-1]))
        num = f.readline()
print(res)
