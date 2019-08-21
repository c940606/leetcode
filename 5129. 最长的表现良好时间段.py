class Solution:
    def longestWPI(self, hours):
        left = 0
        days = 0
        res = 0
        for i in range(len(hours)):
            if hours[i] > 8:
                days += 1
            else:
                days -= 1
            while days <= 0 and left <= i:
                # print(left)

                if hours[left] > 8:
                    days -= 1
                else:
                    days += 1
                left += 1

            print(left, i)
            res = max(res, i - left + 1)
        return res


a = Solution()
# print(a.longestWPI([9, 9, 6, 0, 6, 6, 9]))
print(a.longestWPI([6, 6, 6]))
print(a.longestWPI([6, 9, 9]))
