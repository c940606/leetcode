from itertools import combinations

boxes = int(input())
wu_boxes = list(map(int, input().split()))
contain_boxes = list(map(int, input().split()))
all_sum = sum(wu_boxes)
# 找最少个数
contain_boxes.sort(reverse=True)
tmp = 0
m = None
for idx, contain in enumerate(contain_boxes):
    tmp += contain
    if tmp >= all_sum:
        m = idx
        break
for item in combinations(range(len(contain_boxes)), m + 1):

