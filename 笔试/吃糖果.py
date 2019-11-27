from itertools import groupby
cnt = int(input())
candy = [int(i) for i in input().split()]
# cnt = 5
# candy = [1, 1, 2, 3, 3]
while 1:
    tmp = []
    for val, c in groupby(sorted(candy)):
        a, b = divmod(len(list(c)), 2)
        #print(val, a, b)
        if a != 0:
            tmp.append(a + val)
        if b == 1:
            tmp.append(val)

    if len(set(tmp)) == len(tmp): break
    candy = tmp
print(len(tmp))