def nearest_smaller_number(arr):
    stack = []
    res = []
    for a in arr:
        while stack and stack[-1] >= a:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append("_")
        stack.append(a)
    return res


print(nearest_smaller_number([1, 6, 4, 10, 2, 5]))
print(nearest_smaller_number([1, 2, 0, 2, 5]))
print(nearest_smaller_number([1, 2, 3, 3, 2, 5]))
