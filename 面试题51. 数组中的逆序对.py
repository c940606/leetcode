from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(i, j):
            if j <= i: return 0
            mid = (i + j) // 2
            tmp = []
            cnt = merge(i, mid) + merge(mid + 1, j)
            l = i
            r = mid + 1
            while l <= mid or r <= j:
                if l <= mid and r <= j:
                    if nums[l] <= nums[r]:
                        tmp.append(nums[l])
                        l += 1
                        cnt += r - mid - 1
                    else:
                        tmp.append(nums[r])
                        r += 1
                elif l <= mid:
                    tmp.append(nums[l])
                    l += 1
                    cnt += r - mid - 1
                elif r <= j:
                    tmp.append(nums[r])
                    r += 1
            nums[i:j + 1] = tmp
            return cnt

        return merge(0, len(nums) - 1)


a = Solution()
print(a.reversePairs([7, 5, 6, 4]))
