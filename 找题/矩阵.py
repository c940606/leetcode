from itertools import permutations


def helper(A):
    res = 0
    for item in permutations(A):
        # print(item)
        tmp = []
        for tm in zip(*item):
            tmp.extend(tm)
        cur = float("inf")
        # print(tmp, cur)
        for i in range(1, len(tmp)):
            # print(i, tmp[i], tmp[i-1])
            cur = min(cur, abs(tmp[i] - tmp[i - 1]))
        # print(cur)
        res = max(res, cur)
        #break
    return res


print(helper([[9, 9], [10, 8], [5, 3], [4, 3]]))
print(helper([[3],
              [6],
              [2],
              [5],
              [1],
              [4]]))
