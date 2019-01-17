class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        lookup = []
        for idx,point in enumerate(points):
            lookup.append((point[0]**2+point[1]**2,idx))
        lookup.sort()

        res = []
        for i in range(K):
            res.append(points[lookup[i][1]])
        return res
a = Solution()
print(a.kClosest(points = [[1,3],[-2,2]], K = 1))


