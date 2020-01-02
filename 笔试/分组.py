"""
给定一个数组,分成两组,使得两组差值最小
比如[1, 2 ,3, 4]
分成 [1, 4] 和 [2, 3]
"""


def split_arr(arr, target):
    from collections import defaultdict
    print(target)
    dp = defaultdict(int)
    for a in arr:
        for num in range(target, -1, -1):
            dp[num] = max(dp[num], (dp[num - a] if num - a >= 0 else float("-inf")) + a)
    return dp[target]


arr = [1, 2, 3, 4, 9, 124, 123]
print(split_arr(arr, sum(arr) // 2))
