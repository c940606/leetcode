# w=((d+2*m+3*(m+1)/5+y+y/4-y/100+y/400)%7+1)%7
class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        if m < 3:
            m += 12
            y -= 1
        d1 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return d1[((d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1) % 7]


a = Solution()
print(a.dayOfTheWeek(d=31, m=8, y=2019))
print(a.dayOfTheWeek(d=18, m=7, y=1999))
print(a.dayOfTheWeek(d=15, m=8, y=1993))
print(a.dayOfTheWeek(29, 2, 2016))
