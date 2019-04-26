class Solution:
    def videoStitching(self, clips, T):

        clips = sorted(clips, key=lambda x: (x[0], x[1]))
        if clips[0][0] != 0:
            return -1
        print(clips)
        n = len(clips)
        i = 0
        j = n - 1
        res = 1
        while i < j:

            while i < n - 1 and clips[i][0] == clips[i + 1][0]:
                i += 1
            while j > 0 and clips[j - 1][1] == clips[j][1]:
                j -= 1
            print(i, j)
            if i == j or clips[i][1] >= T:
                break
            if clips[i][1] < clips[j][0]:
                j -= 1
            else:
                # print(i,j)
                res += 1
                i = j
                j = n - 1
        if clips[i][1] >= T:
            return res
        else:
            return -1

    def videoStitching1(self, clips, T):
        from collections import deque
        queue = deque()
        visited = set()
        for x, y in clips:
            if x == 0:
                visited.add((x, y))
                queue.append((y, 1))
        if not queue:
            return -1
        while queue:
            end, step = queue.pop()
            if end >= T:
                return step
            for x, y in clips:
                if (x, y) not in visited:
                    if end >= x:
                        queue.appendleft((y, step + 1))
                        visited.add((x, y))
        return -1

    def videoStitching2(self, clips, T):
        clips.sort()
        # print(clips)
        n = len(clips)
        dp = [float("inf")] * n
        if clips[0][0] != 0:
            return -1
        for i in range(n):
            if clips[i][0] == 0:
                dp[i] = 1
            else:
                break
        for i in range(n):
            for j in range(i):
                if dp[j] != float("inf") and clips[j][1] >= clips[i][0]:
                    dp[i] = min(dp[i], dp[j] + 1)
        # print(dp)
        res = float("inf")
        for i in range(n):
            if clips[i][1] >= T:
                res = min(res, dp[i])
        return res if res != float("inf") else -1

    def videoStitching3(self, clips, T):
        left, right, res = -1, 0, 0
        for x, y in sorted(clips):
            if right >= T or x > right:
                break
            elif left < x <= right:
                res, left = res + 1, right
            right = max(right, y)
        return res if right >= T else -1


a = Solution()
print(a.videoStitching3(clips=[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T=10))
# print(a.videoStitching1(clips = [[0,1],[1,2]], T = 5))
# print(a.videoStitching1(
#     clips=[[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
#            [4, 5], [5, 7], [6, 9]], T=9))
# print(a.videoStitching(clips = [[0,4],[2,8]], T = 5))
# # print(a.videoStitching([],None))
# print(a.videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]],5))
# print(a.videoStitching1([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]],5))
# print(a.videoStitching1([[8,10],[17,39],[18,19],[8,16],[13,35],[33,39],[11,19],[18,35]],20))
# print(a.videoStitching1([[16,18],[16,20],[3,13],[1,18],[0,8],[5,6],[13,17],[3,17],[5,6]],15))
