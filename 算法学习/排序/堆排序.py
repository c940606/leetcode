def heap_sort(nums):
    # 调整堆
    # 迭代写法
    def adjust_heap(nums, startpos, endpos):
        newitem = nums[startpos]
        pos = startpos
        childpos = pos * 2 + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and nums[rightpos] >= nums[childpos]:
                childpos = rightpos
            if newitem < nums[childpos]:
                nums[pos] = nums[childpos]
                pos = childpos
                childpos = pos * 2 + 1
            else:
                break
        nums[pos] = newitem

    # 递归写法
    def adjust_heap(nums, startpos, endpos):
        pos = startpos
        chilidpos = pos * 2 + 1
        if chilidpos < endpos:
            rightpos = chilidpos + 1
            if rightpos < endpos and nums[rightpos] > nums[chilidpos]:
                chilidpos = rightpos
            if nums[chilidpos] > nums[pos]:
                nums[pos], nums[chilidpos] = nums[chilidpos], nums[pos]
                adjust_heap(nums, pos, endpos)

    n = len(nums)
    # 建堆
    for i in reversed(range(n // 2)):
        adjust_heap(nums, i, n)
    # 调整堆
    for i in range(n - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        adjust_heap(nums, 0, i)
    return nums

print(heap_sort([]))
print(heap_sort([1, 2, 6, 3, 5, 2]))
