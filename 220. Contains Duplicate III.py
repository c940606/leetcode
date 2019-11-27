from 数据结构.BST import BST, DList, DLNode, BSTNode
from collections import deque


class Solution:
    def containsNearbyAlmostDuplicate1(self, nums, k, t):
        nums_loc = []
        for idx, num in enumerate(nums):
            nums_loc.append([num, idx])
        nums_loc.sort()
        n = len(nums)
        # print(nums_loc)
        for i in range(n):
            for j in range(i + 1, n):
                if nums_loc[j][0] - nums_loc[i][0] > t:
                    break
                if abs(nums_loc[i][1] - nums_loc[j][1]) <= k:
                    return True
        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        from collections import deque
        import bisect
        n = len(nums)
        if n <= 1: return False
        m = min(n, k + 1)
        queue = sorted(nums[:m])
        to_del = deque()
        to_del.extendleft(nums[:m])
        for i in range(1, m):
            if queue[i] - queue[i - 1] <= t:
                return True
        print(queue)
        for i in range(m, n):
            queue.remove(to_del.pop())
            queue.append(nums[i])
            queue.sort()
            loc = queue.index(nums[i])
            # loc = bisect.bisect_left(queue, nums[i])
            # queue.insert(loc, nums[i])
            # print(queue, loc)
            if (loc - 1 >= 0 and nums[i] - queue[loc - 1] <= t) or \
                    (loc + 1 <= k and queue[loc + 1] - nums[i] <= t):
                return True
            to_del.appendleft(nums[i])

        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        from collections import OrderedDict
        n = len(nums)
        if n <= 1 or k == 0: return False
        queue = OrderedDict()
        for n in nums:

            key = n if not t else n // t
            #print(queue, key, n)
            for m in [queue.get(key - 1), queue.get(key), queue.get(key + 1)]:
                #print(m)
                if m is not None and abs(n - m) <= t:
                    return True
            if len(queue) == k:
                queue.popitem(False)
            queue[key] = n
        return False

    def containsNearbyAlmostDuplicate3(self, nums, k: int, t: int) -> bool:
        if not nums or k == 0:
            return False

        n = len(nums)
        m = DLNode(nums[0])
        bst = BST(m)
        toDel = deque([m])
        for x in nums[1:k + 1]:
            m = DLNode(x)
            _, _ = bst.insert(m)
            toDel.append(m)

        for i, m in enumerate(bst.popByorder()):
            if i == 0:
                dl = DList(m)
            else:
                dl.append(m)

        i, j = dl.head, dl.head.next
        while j:
            if j.v - i.v <= t:
                return True
            i = i.next
            j = j.next

        if k < n:
            for x in nums[k + 1:]:
                d = toDel.popleft()
                bst.delNode(d)
                m = DLNode(x)
                l, r = bst.insert(m)
                if (l and m.v - l.v <= t) or (r and r.v - m.v <= t):
                    return True
                toDel.append(m)
        return False


a = Solution()
print(a.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
print(a.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))
print(a.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
print(a.containsNearbyAlmostDuplicate([-3, 3], 2, 4))
print(a.containsNearbyAlmostDuplicate([10, 100, 11, 9], 1, 2))
print(a.containsNearbyAlmostDuplicate([1, 2], 0, 1))
print(a.containsNearbyAlmostDuplicate([3, 6, 0, 2], 2, 2))
