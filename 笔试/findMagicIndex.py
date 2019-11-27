def findMagicIndex(A):
    n = len(A)
    if n == 0: return True
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if mid == A[mid]:
            return True
        elif mid > A[mid]:
            left = mid + 1
        else:
            right = mid
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if mid == A[mid]:
            return True
        elif mid > A[mid]:
            right = mid
        else:
            left = mid + 1
    return False


print(findMagicIndex([1, 3, 5, 5, 5, 5, 7, 8, 9, 10, 11, 12]))
print(findMagicIndex([1,1,3,4,5]))
