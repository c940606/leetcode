class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        res = 0
        n = len(calories)
        for i in range(0, n - k + 1):
            tmp = sum(calories[i:i + k])
            #print(i, i+k, tmp)
            if tmp < lower:
                res -= 1
            elif tmp > upper:
                res += 1
        return res
a = Solution()
print(a.dietPlanPerformance(calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3))
print(a.dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1))
print(a.dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5))
print(a.dietPlanPerformance([6,13,8,7,10,1,12,11],6,5,37))