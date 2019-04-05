class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        reach_target = []
        n = len(position)
        for i in range(n):
            reach_target.append(((target - position[i]) / speed[i], position[i]))
        reach_target.sort()
        dp = [None] * n
        dp[-1] = reach_target[-1][1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i+1],reach_target[i][1])
        #print(dp)
        return len(set(dp))


a = Solution()
print(a.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print(a.carFleet(10, [0, 4, 2], [2, 1, 3]))
