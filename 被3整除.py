l,r = map(int,input().split())

tmp = ""
res = 0
for i in range(1,l):
    tmp += str(i)
for j in range(l,r+1):
    tmp += str(j)
    if int(tmp) % 3 == 0:
        res += 1

print(res)