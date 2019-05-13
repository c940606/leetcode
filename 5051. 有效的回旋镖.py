class Solution:
    def isBoomerang(self, points):
        a1, b1 = points[0]
        a2, b2 = points[1]
        a3, b3 = points[2]
        p1_p2 = [a1 - a2, b1 - b2]
        p1_p3 = [a1 - a3, b1 - b3]
        return p1_p2[0] * p1_p3[1] != p1_p2[1] * p1_p3[0]


a = Solution()
print(a.isBoomerang([[1, 1], [2, 3], [3, 2]]))
print(a.isBoomerang([[1, 1], [2, 2], [3, 3]]))
print(a.isBoomerang([[0,0],[0,2],[2,1]]))
