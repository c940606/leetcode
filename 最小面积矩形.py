class Solution(object):
	def minAreaRect(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""
		if not points:
			return 0
		lookup = {}
		for point in points:
			if point[0] in lookup:
				lookup[point[0]].append(point[1])
			else:
				lookup[point[0]] = [point[1]]
		# print(lookup)
		keys = list(lookup.keys())
		for key in keys:
			# print(key,value)
			if len(lookup[key])<=1:
				del lookup[key]


		print(lookup)
		row = list(lookup.keys())
		res = 100000000000000
		flag = 0
		for i in row:
			for j in row:
				if i == j:
					continue
				set1 = sorted(list(set(lookup[i])&set(lookup[j])))
				if len (set1) < 2:
					continue
				temp = min(map(lambda x:abs(x[0]-x[1]),zip(set1,set1[1:])))
				flag = 1
				res = min(abs(i-j)*temp,res)
		return res if flag == 1 else 0

a = Solution()
# print(a.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
# print(a.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
# print(a.minAreaRect([[3,2],[0,0],[3,3],[3,4],[4,4],[2,1],[4,3],[1,0],[4,1],[0,2]]))
# print(a.minAreaRect([[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]))
# print(a.minAreaRect([[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]))
print(a.minAreaRect([[26737,17514],[22235,25740],[3813,25740],[26737,7819],[29299,28174],[26737,8831],[22235,17514],[22236,28174],[35250,7819],[22236,8831],[29299,19727],[3813,17514],[22236,7819],[22235,1333],[35250,19727],[35250,28174],[22236,19727],[3813,19727],[35250,8831],[3813,8831],[35250,25740],[3813,28174],[29299,25740],[3813,1333],[29299,8831],[36784,7819],[36784,8831],[22235,28174],[3813,7819],[26737,1333],[29299,1333],[29299,7819],[36784,25740]]))