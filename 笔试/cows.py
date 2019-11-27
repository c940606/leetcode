import functools
# @functools.lru_cache(None)
def cows(n):
    if n == 0:
        return 0
    if n in {1, 2, 3}:
        return 1
    return cows(n - 3) + cows(n - 1)

print(cows(20))