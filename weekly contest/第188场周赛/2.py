from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0]
        for a in arr:
            prefix.append(prefix[-1] ^ a)
        """:arg
        arr[i:j] = prefix[0:j] ^ prefix[0: i - 1]
        
        arr[i:j - 1] = prefix[0:j - 1] ^ prefix[0:i - 1]
        arr[k:j] = prefix[0:k] ^ prefix[0:j - 1]
    
        """
        res = 0

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                for k in range(j, n + 1):
                    if prefix[j - 1] ^ prefix[i - 1] == prefix[k] ^ prefix[j - 1]:
                        print(i, j, k)
                        res += 1

        return res


a = Solution()
# print(a.countTriplets([2, 3, 1, 6, 7]))
print(a.countTriplets([1, 1, 1, 1, 1]))
# print(a.countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))
# print(a.countTriplets([1,3,5,7,9]))
# print(a.countTriplets([2,3]))
