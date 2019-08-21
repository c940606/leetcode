class Solution:
    def getModifiedArray(self, length, updates):
        res = [0] * length

        def helper(start, end, inc):
            for i in range(start, end + 1):
                res[i] += inc

        for update in updates:
            helper(*update)
        return res

    def getModifiedArray1(self, length, updates):
        nums = [0] * length
        for i, j, x in updates:
            nums[i] += x
            nums[j + 1] -= x
        res = []
        tmp = 0
        for num in nums:
            tmp += num
            res.append(tmp)
        return res

    def getModifiedArray2(self, length, updates):
        res = [0] * (length + 1)
        for i, j, x in updates:
            res[i] += x
            res[j+1] -= x
        for i in range(1,length):
            res[i] += res[i-1]
        return res[:-1]