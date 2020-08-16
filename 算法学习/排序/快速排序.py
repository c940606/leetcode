def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums
        pivot = left
        i = left
        j = right
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        quick(left, j - 1)
        quick(j + 1, right)
        return nums

    return quick(0, n - 1)

print(quick_sort([]))
print(quick_sort([2, 1, 1, 1, 5, 5, 5]))
print(quick_sort([3, 2, 1]))
print(quick_sort([0, 1, 2, 1]))
# [3,1, 5, 2, 7]
# [2, 5, 1, 1,1]
