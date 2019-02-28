def adjust_heap(array, i, n):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max_loc = i
    if i < n /2:
        if lchild < n and array[lchild] > array[max_loc]:
            max_loc = lchild
        if rchild < n and array[rchild] > array[max_loc]:
            max_loc = rchild
        if max_loc != i:
            array[max_loc],array[i] = array[i],array[max_loc]
            adjust_heap(array,max_loc,n)
def build_heap(array, n):
    for i in range(n // 2, -1, -1):
        adjust_heap(array, i, n)
        print(array)
def heap_sort(array):
    n = len(array)
    build_heap(array, n)
    for i in range(n-1,-1,-1):
        array[i],array[0] = array[0],array[i]
        adjust_heap(array,0,i)
    return array

a = [50, 16, 30, 10, 60,  90,  2, 80, 70]
print(heap_sort(a))

def adjust_heap(array,i,n):
    lchild = i * 2 + 1
    rchild = i*2 + 2
    max_loc = i
    if i < n/2:
        if lchild < n and array[lchild] > array[max_loc]:
            max_loc = lchild
        if rchild < n and array[rchild] > array[max_loc]:
            max_loc = rchild
        if i!= max_loc:
            array[max_loc],array[i] = array[i],array[max_loc]
            adjust_heap(array,max_loc,n)
def build_heap(array,n):
    for i in range(n//2,-1,-1):
        adjust_heap(array,i,n)

def sort_heap(array):
    n = len(array)
    build_heap(array,n)
    for i in range(n-1,-1,-1):
        array[0],array[i] = array[i] ,array[0]
        adjust_heap(array,0,i)
    return array
