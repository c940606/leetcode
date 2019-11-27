def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    mid = n // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    i = 0
    j = 0
    # print(left, right)
    while i < len(left) or j < len(right):
        if j == len(right) or i < len(left) and left[i] <= right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1
    return arr

lists = [3, 5, 4, 2, 1, 6]
# print(merge_sort(lists))
print(mergeSort(lists))
