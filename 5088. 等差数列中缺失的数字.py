from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        tmp = []
        for i in range(len(arr) - 1):
            tmp.append(arr[i + 1] - arr[i])
        max_num = max(tmp, key=abs)
        for idx in range(len(tmp)):
            if tmp[idx] == max_num:
                return arr[idx] + max_num // 2


a = Solution()
print(a.missingNumber([15, 13, 12]))
