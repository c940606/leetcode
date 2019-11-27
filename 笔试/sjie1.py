import bisect


def getMininumMoves(arr):
    # stack = []
    # for num in arr:
    #     if not stack or stack[-1] < num:
    #         stack.append(num)
    #     else:
    #         loc = bisect.bisect_left(stack, num)
    #         stack[loc] = num
    #     # print(stack)
    # return len(stack)
    if not arr:
        return 0
    maxCount, count = 1, 1
    for i in range(len(arr) - 1):
        # 处于递增中
        if arr[i + 1] > arr[i]:
            count += 1
        else:
            # 计算最大长度
            maxCount = max(maxCount, count)
            count = 1
    # 最大长度在数组末尾的情况
    return len(arr) - max(maxCount, count)




if __name__ == '__main__':
    num = int(input())
    arr = []
    for _ in range(num):
        arr.append(int(input()))

    print(getMininumMoves(arr))
