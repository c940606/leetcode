def bubbleSort(array):
    n = len(array)
    f = n - 1
    for _ in range(n - 1):
        for i in range(f):
            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
        f -= 1
    return array


a = [2, 3, 3, 4, 1, 6]
b = [5, 4, 5, 7, 9, 3, 2, 3, 4]
print(bubbleSort(b))
