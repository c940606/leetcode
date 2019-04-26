from collections import defaultdict

# source = "abc"
# target = "abcbc"
# source = "abc"
# target = "acdbc"
source = "xyz"
target = "xzyxz"
lookup = defaultdict(list)
for idx, alp in enumerate(source):
    lookup[alp].append(idx)
res = 0
i = 0
while i < len(target):
    loc = source.find(target[i])
    if loc == -1:
        print(-1)
        break
    while i < len(target) - 1 and loc < source.find(target[i + 1], loc + 1, len(source)):
        loc = source.find(target[i + 1], loc + 1, len(source))
        i += 1
    res += 1
    i += 1
print(res if res != 0 else -1)
