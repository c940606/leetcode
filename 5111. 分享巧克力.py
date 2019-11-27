from typing import List
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left = 1
        right = sum(sweetness) + 1
        def check(mid):
            cnt = 0
            tmp = 0
            for sw in sweetness:
                tmp += sw
                if tmp >= mid:
                    cnt += 1
                    tmp = 0
            #print(cnt)
            return cnt >= K + 1
        # print(check(6))
        while left <= right:
            #print(left, right)
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right

a = Solution()
print(a.maximizeSweetness(sweetness = [1,2,3,4,5,6,7,8,9], K = 5))
print(a.maximizeSweetness(sweetness = [5,6,7,8,9,1,2,3,4], K = 8))
print(a.maximizeSweetness(sweetness = [1,2,2,1,2,2,1,2,2], K = 2))
