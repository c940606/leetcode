happiness = [list(map(int, input().split())) for _ in range(int(input()))]

n = len(happiness)
#
for i in range(1, n):
    for j in range(3):
        cur = float("-inf")
        for k in range(3):
            if j != k:
                cur = max(happiness[i - 1][k], cur)
        happiness[i][j] += cur
# print(happiness)
print(max(happiness[-1]))
