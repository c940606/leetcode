def betterCompression(s):
    from collections import defaultdict
    i = 0
    n = len(s)
    lookup = defaultdict(int)
    while i < n:
        if s[i].isalpha():
            k = s[i]
            i += 1
        num = ""
        while i < n and s[i].isdigit():
            num += s[i]
            i += 1
        lookup[k] += int(num)
    res = ""
    for k, v in sorted(lookup.items(), key=lambda x: x[0]):
        res += (k + str(v))
    return res


print(betterCompression("a12b56c1a1"))
print(betterCompression("a12c56a1b5"))