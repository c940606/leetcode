def quick_sort(array):
    n = len(array)
    def helper(array, left, right):
        if left >= right:
            return array
        base = array[left]
        ln = left
        rn = right
        while left < right:
            while left < right and array[right] >= base:
                right -= 1
            while left < right and array[left] <= base:
                left += 1
            array[left], array[right] = array[right], array[left]
        array[left], array[ln] = array[ln], array[left]
        helper(array, ln, left - 1)
        helper(array, left + 1, rn)
        return array

    return helper(array, 0, n - 1)


def quick_sort1(arr, left, right):
    if left >= right:
        return arr
    pivot = arr[left]  # 取第一个元素为哨兵
    low = left  # 保留初始的left和right的值，后面要用
    high = right
    while left < right:
        while left < right and arr[right] >= pivot:  # 从右向左,找到第一个比pivot小的元素
            right -= 1
        arr[left] = arr[right]  # 把该右边值放到左边位置上
        while left < right and arr[left] < pivot:  # 从左向右，找到第一个比pivot大的元素
            left += 1
        arr[right] = arr[left]  # 把该左边值放到右边位置上
    arr[right] = pivot  # 此时，left和right指向同一个位置
    quick_sort1(arr, low, left - 1)
    quick_sort1(arr, right + 1, high)
    return arr

def quick_sort3(array):
    n = len(array)
    def helper(array,left,right):
        if left >= right:
            return array
        base = array[left]
        ln = left
        rn = right
        while left < right:
            while left < right and array[right] >= base:
                right -= 1
            while left < right and array[left] <= base:
                left += 1
            array[left],array[right] = array[right],array[left]
        array[left],array[ln] = array[ln],array[left]
        helper(array,ln,left-1)
        helper(array,right+1,rn)
        return array
    return helper(array,0,n-1)
b = [5, 4, 5, 7, 9, 3, 2, 3, 4]
print(quick_sort3(b))
