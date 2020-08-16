def bucket_sort(nums, bucketSize):
    if len(nums) < 2:
        return nums
    _min = min(nums)
    _max = max(nums)
    # 需要桶个数
    bucketNum = (_max - _min) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        # 放入相应的桶中
        buckets[(num - _min) // bucketSize].append(num)
    res = []

    for bucket in buckets:
        if not bucket: continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            # 当都装在一个桶里,说明桶容量大了
            if bucketNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort(bucket, bucketSize))
    return res


print(bucket_sort([1, 2, 5, 3, 2, 1, 234, 23, 1, 23, 5, 31], 5))
