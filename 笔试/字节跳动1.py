from collections import defaultdict

# 单调递减
# m = int(input())
# heights = list(map(int, input().split()))
m = 4
# heights = [0] + [6, 5, 3, 4] + [0]
heights = [0] + [1, 2, 3]
lookup = defaultdict(int)
stack = []
for h in heights:
    while stack and stack[-1] < h:
        stack.pop()
    if stack:
        lookup[stack[-1]] += 1
    # print(stack)
    stack.append(h)
print(lookup)
# if not lookup:rint(0)
# else:
print(sorted(lookup.items(), key=lambda x: (-x[1], x[0]))[0][0])
