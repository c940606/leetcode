class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        flag = 0
        for a in arr:
            if a != 0 and a * 2 in arr:
                return True
            if a == 0:
                flag += 1
        return True if flag >= 2 else False


a = Solution()
print(a.checkIfExist())