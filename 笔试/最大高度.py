def max_height1(heights):
    import bisect
    queue = []
    res = 0
    for i, height in enumerate(heights):
        if not queue or -queue[-1][0] > height:
            queue.append([-height, i])
        else:
            loc = bisect.bisect(queue, [-height])
            #print(queue, height, loc)
            res = max(res, i - loc)
    return res
def max_height2(heights):
    res = 0
    now = 0
    queue = []
    for i, height in enumerate(heights):
        if not queue or queue[-1][0] > height:
            queue.append([height, i])
        else:
            while now + 1 < len(queue) and i - queue[now + 1][1] > res:
                now += 1
            while now - 1 >= 0 and height >= queue[now - 1][0]:
                now -= 1
            if height >= queue[now][0]:
                res = i - queue[now][1]
    return res




print(max_height2([6, 0, 8, 2, 1, 5]))
print(max_height1([5, 5, 5]))
