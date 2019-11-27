data = []
for i in range(7):
    data.append([sum(map(int, input().split())), i + 1])
data.sort(key=lambda x: (-x[0], x[1]))

print(data[0][1])
