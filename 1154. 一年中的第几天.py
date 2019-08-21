class Solution:
    def ordinalOfDate(self, date: str) -> int:
        arr =  [0,31,28,31,30,31,30,31,31,30,31,30,31]

        def helper(year):
            if year % 4 == 0 and year % 100 != 0 or year% 400 ==0:
                return True
            return False
        str_s = date.split("-")
        if helper(int(str_s[0])):
            arr[2] = 29
        res = 0
        for i in range(1, int(str_s[1])):
            res += arr[i]
        res += int(str_s[2])
        return res

a = Solution()
print(a.ordinalOfDate("2019-01-09"))
print(a.ordinalOfDate("2003-03-01"))
print(a.ordinalOfDate("2004-03-01"))