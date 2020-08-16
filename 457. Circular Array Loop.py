from typing import List
import sys
sys.setrecursionlimit(500000)

class Solution:
    def circularArrayLoop1(self, nums: List[int]) -> bool:
        from collections import defaultdict
        n = len(nums)

        def dfs(cur, flag, l, visited):
            if (nums[cur] > 0) != flag:
                return False
            if cur in visited:
                if l - visited[cur] > 1:
                    return True
                else:
                    return False
            visited[cur] = l
            if dfs((nums[cur] + cur) % n, flag, l + 1, visited):
                return True
            return False

        for i in range(n):
            # 参数: 下一个位置, 正负号记号, 长度, 字典记录长度
            if dfs((nums[i] + i) % n, nums[i] > 0, 1, defaultdict(int)):
                return True
        return False

    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)
        nxt = lambda x: (x + nums[x]) % n

        for i in range(n):
            if nums[i] == 0: continue
            slow = i
            fast = nxt(i)
            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nxt(fast)] > 0:
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    else:
                        return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))
            val = nums[i]
            while val * nums[i] > 0:
                tmp = nxt(i)
                nums[i] = 0
                i = tmp
        return False


a = Solution()
print(a.circularArrayLoop1([1] * 5000))
# print(a.circularArrayLoop([2, 1, 1, -1]))  # false
# print(a.circularArrayLoop([2, 2, 2, 2, 2, 4, 7]))  # false
# print(a.circularArrayLoop([-2, 1, -1, -2, -2]))
# print(a.circularArrayLoop([2, -1, 1, 2, 2]))
# print(a.circularArrayLoop([-1, 2]))
# print(a.circularArrayLoop([2, -1, 1, -2, -2]))
# print(a.circularArrayLoop([-1, -2, -3, -4, -5]))
