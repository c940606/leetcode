from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            cnt = 0
            copy_arr = arr.copy()
            for i in range(1, len(arr) - 1):
                if copy_arr[i - 1] < copy_arr[i] and copy_arr[i] > copy_arr[i + 1]:
                    arr[i] -= 1
                    cnt += 1
                elif copy_arr[i - 1] > copy_arr[i] and copy_arr[i] < copy_arr[i + 1]:
                    arr[i] += 1
                    cnt += 1
            if cnt == 0:
                break
        return arr

a = Solution()
print(a.transformArray([6,2,3,4]))
print(a.transformArray([1,6,3,4,3,5]))
print(a.transformArray([2,1,2,1,1,2,2,1]))