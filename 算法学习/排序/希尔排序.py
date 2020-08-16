def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i - gap >= 0 and nums[i - gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i - gap]
                i -= gap
        gap //= 2
    return nums

print(shell_sort([]))
print(shell_sort([4, 5, 2, 3, 2, 1]))
