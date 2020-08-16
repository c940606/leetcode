def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(selection_sort([4, 5, 2, 3, 2, 1]))
