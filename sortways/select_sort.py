def select_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i, n):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array
b  =[5,4,5,7,9,3,2,3,4]
print(select_sort(b))
