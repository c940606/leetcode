# Python 实现的十大经典排序算法

参考链接：https://blog.csdn.net/MobiusStrip/article/details/83785159?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

## 需求

对一个无序数组，根据某个关键字排序。

## 划分方法

排序算法划分方法有：稳定性，内外排序，时空复杂度

按照**稳定性**划分，稳定排序，如果`a`原本在`b`前面，而`a=b`，排序之后`a`仍然在`b`的前面；而不稳定可能出现在`b`之后。

按照**内外排序**划分，内排序，所有排序操作都在内存中完成；外排序 ：由于数据太大，因此把数据放在磁盘中，而排序通过磁盘和内存的数据传输才能进行；

按照**时空复杂度**划分，时间复杂度是指运行时间，空间复杂度运行完一个程序所需内存的大小。

## 常见排序方法

###  选择排序（Selection Sort）



![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015224719590-1433219824.gif)

这应该最符合人类思维的排序方法，工作原理，首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

稳定性：稳定；内排序；

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
```

算法分析：

时间复杂度：$O(n^2)$ ，`n`是数组长度



###  冒泡排序（Bubble Sort）

冒泡排序时针对**相邻元素之间**的比较，可以将大的数慢慢“沉底”(数组尾部)

![](D:\learning\algorithm\leetcode\算法学习\排序\v2-d4c88b8cc620af6af67c33910899fcf7_b.gif)

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015223238449-2146169197.gif)

```python
def bubble_sort(nums):
    n = len(nums)
    # 进行多次循环
    for c in range(n):
        for i in range(1, n - c):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
    return nums
```

稳定排序，内排序，时间复杂度：$O(n^2)$

###  插入排序（Insertion Sort）

插入排序是前面**已排序数组**找到插入的位置

![](D:\learning\algorithm\leetcode\算法学习\排序\Insertion-sort-example-300px.gif)

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015225645277-1151100000.gif)

```python
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1
    return nums
```

算法分析：

稳定排序，内排序，时间复杂度：$O(n^2)$

###  希尔排序（Shell Sort）

插入排序进阶版，

**算法描述：**

 我们来看下希尔排序的基本步骤，在此我们选择增量`gap=length/2`，缩小增量继续以`gap = gap/2`的方式，这种增量选择我们可以用一个序列来表示，`{n/2,(n/2)/2…1}`，称为增量序列。希尔排序的增量序列的选择与证明是个数学难题，我们选择的这个增量序列是比较常用的，也是希尔建议的增量，称为希尔增量，但其实这个增量序列不是最优的。

先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

- 步骤1：选择一个增量序列$t_1，t_2，…，t_k$，其中$t_i>t_j，t_k=1$；

- 步骤2：按增量序列个数k，对序列进行k 趟排序；

- 步骤3：每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

  ![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20180331170017421-364506073.gif)

![image](D:\learning\algorithm\leetcode\算法学习\排序\1192699-20180319094116040-1638766271.png)

```python
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
```

算法分析：

非稳定排序，内排序；

希尔排序的时间复杂度和增量序列是相关的。

`{1,2,4,8,...}`这种序列并不是很好的增量序列，使用这个增量序列的时间复杂度（最坏情形）是$O(n^2)$；

`Hibbard`提出了另一个增量序列${1,3,7，...,2^k-1}$，这种序列的时间复杂度(最坏情形)为$O(n^{1.5})$；

`Sedgewick`提出了几种增量序列，其最坏情形运行时间为$O(n^{1.3})$，其中最好的一个序列是`{1,5,19,41,109,...}`；

对于不同增量的复杂度感兴趣可以参考《数据结构与算法分析》一书或其他相关论文。

###  归并排序（Merge Sort）

归并排序，采用是分治法，先将数组分成子序列，让子序列有序，再将子序列间有序，合并成有序数组。

算法描述：

1. 把长度为`n`的输入序列分成长度 `n/2`的子序列；
2. 对两个子序列采用归并排序；
3. 合并所有子序列。

![](D:\learning\algorithm\leetcode\算法学习\排序\1252882-20190217215522179-1982419775.gif)

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015230557043-37375010.gif)

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    # 分
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    # 合并
    return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res
```

算法分析：

稳定排序，外排序（占用额外内存），时间复杂度$O(nlogn)$。

###  快速排序（Quick Sort）

快速排序是选取一个“哨兵”(`pivot`)，将小于`pivot`放在左边，把大于`pivot`放在右边，分割成两部分，并且可以固定`pivot`在数组的位置，在对左右两部分继续进行排序。

快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

- 步骤1：从数列中挑出一个元素，称为 “基准”（**pivot** ）；
- 步骤2：重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 步骤3：递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

![](D:\learning\algorithm\leetcode\算法学习\排序\Quicksort-example.gif)

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015230936371-1413523412.gif)

```python
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
```

算法分析：

不稳定排序，内排序，时间复杂度度$O(nlogn)$。

###  堆排序（Heap Sort）

堆排序是利用堆这个数据结构设计的排序算法。

算法描述：

1. 建堆，从底向上调整堆，使得父亲节点比孩子节点值大，构成大顶堆；
2. 交换堆顶和最后一个元素，重新调整堆。

调整堆方法写了递归和迭代，都很好理解！



![](D:\learning\algorithm\leetcode\算法学习\排序\Heapsort-example.gif)

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015231308699-356134237.gif)

```python
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
```

算法分析：

不稳定排序，内排序，时间复杂度为$O(nlogn)$。

###  计数排序（Counting Sort）

计数排序是典型的空间换时间算法，开辟额外数据空间存储用索引号记录数组的值和数组值个数

算法描述：

1. 找出待排序的数组的最大值和最小值
2. 统计数组值的个数
3. 反向填充目标数组

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015231740840-6968181.gif)

```python
def counting_sort(nums):
    if not nums: return []
    n = len(nums)
    _min = min(nums)
    _max = max(nums)
    tmp_arr = [0] * (_max - _min + 1)
    for num in nums:
        tmp_arr[num - _min] += 1
    j = 0
    for i in range(n):
        while tmp_arr[j] == 0:
            j += 1
        nums[i] = j + _min
        tmp_arr[j] -= 1
    return nums

```

算法分析：

稳定排序，外排序，时间复杂度$O(n + k)$，但是对于数据范围很大的数组，需要大量时间和内存。

###  桶排序（Bucket Sort）

桶排序是计数排序的升级版，原理是：输入数据服从均匀分布的，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的算法或是以递归方式继续使用桶排序，此文编码采用递归方式）

算法描述：

1. 人为设置一个桶的`BucketSize`，作为每个桶放置多少个**不同数值**（意思就是`BucketSize = 5`，可以放5个不同数字比如`[1, 2, 3,4,5]`也可以放 `100000`个`3`，只是表示该桶能存几个不同的数值）
2. 遍历待排序数据，并且把数据一个一个放到对应的桶里去
3. 对每个不是桶进行排序，可以使用其他排序方法，也递归排序
4. 不是空的桶里数据拼接起来



![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015232107090-1920702011.png)

```python
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
```

算法分析：

稳定排序，外排序，时间复杂度$O(n + k)$，`k`为桶的个数。

###  基数排序（Radix Sort）

基数排序是对数字每一位进行排序，从最低位开始排序

算法描述：

1. 找到数组最大值，得最大位数；
2. 从最低位开始取每个位组成`radix`数组；
3. 对`radix`进行计数排序（计数排序适用于小范围的特点）。

![img](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015232453668-1397662527.gif)



```python
def Radix_sort(nums):
    if not nums: return []
    _max = max(nums)
    # 最大位数
    maxDigit = len(str(_max))
    bucketList = [[] for _ in range(10)]
    # 从低位开始排序
    div, mod = 1, 10
    for i in range(maxDigit):
        for num in nums:
            bucketList[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for item in bucketList[j]:
                nums[idx] = item
                idx += 1
            bucketList[j] = []
    return nums
```

算法分析：

稳定排序，外排序，时间复杂度 $posCount  * (n  + n)$ ，其中 `posCount` 为数组中最大元素的最高位数；简化下得：$O( k *n ) $；其中k为常数，n为元素个数。

## 算法总结

![image](D:\learning\algorithm\leetcode\算法学习\排序\849589-20171015233043168-1867817869.png)

**图片名词解释：**

- n: 数据规模
- k: “桶”的个数
- In-place: 占用常数内存，不占用额外内存
- Out-place: 占用额外内存

