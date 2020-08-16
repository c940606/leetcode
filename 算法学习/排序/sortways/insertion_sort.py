def insertions_sort(array):
    n = len(array)
    for i in range(1,n):
        tmp = array[i]
        j = i - 1
        while j >= 0 and array[j] > tmp:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = tmp
    return array
a = [2,3,3,4,1,6]
b = [5,4]
print(insertions_sort(a))