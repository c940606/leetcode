def partitionLabels(S):
    i = 0
    res = []
    while i < len(S):
        left = i
        right = S.rindex(S[i])
        for j in range(i, len(S)):
            last = S.rindex(S[j])
            if last > right:
                right = last
            elif j == right:
                res.append(right - left + 1)
                i = right + 1
                break
    return res


if __name__ == "__main__":
    s = input()
    tmp = partitionLabels(s)
    b = [str(i) for i in tmp]
    result = ",".join(b)
    print(result)
