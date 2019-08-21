class Solution:
    def minSwaps(self, data) -> int:
        L = sum(data)
        cur = L - sum(data[:L])
        res = cur
        left = 0
        right = L
        while right < len(data):
            if data[left] == 0: cur -= 1
            if data[right] == 0: cur += 1
            res = min(cur, res)
            left += 1
            right += 1
        return res

    # def minSwaps(self, data) -> int:


a = Solution()
# print(a.minSwaps([1, 0, 1, 0, 1]))
# print(a.minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
print(a.minSwaps([0, 0, 0, 1, 0]))
