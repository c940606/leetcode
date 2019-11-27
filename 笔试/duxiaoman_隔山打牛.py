def cattle(bloods):
    bloods = [0] + bloods
    n = len(bloods)
    cur = n
    res = 0
    while cur > -1:
        if cur * 2 >= n or cur * 2 + 1 >= n:
            cur -= 1
            continue
        max_num = max(bloods[cur * 2], bloods[cur * 2 + 1])
        bloods[cur * 2], bloods[cur * 2 + 1] = 0, 0
        bloods[cur] = max(0, bloods[cur] - max_num)
        res += max_num
        cur -= 1
        # print(bloods)
    return res


if __name__ == '__main__':
    n = int(input())
    bloods = list(map(int, input().split()))
    print(cattle(bloods))
