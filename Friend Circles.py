class Solution(object):
	def findCircleNum(self, M):
		"""
		班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
		如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
		给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，
		表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数
		---
		输入:
		[[1,1,0],
		 [1,1,0],
		 [0,0,1]]
		输出: 2
		说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
		第2个学生自己在一个朋友圈。所以返回2。
		---
		输入:
		[[1,1,0],
		 [1,1,1],
		 [0,1,1]]
		输出: 1
		说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，
		所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
		:type M: List[List[int]]
		:rtype: int
		"""
		people = len(M)
		res = 0
		visited = set()

		def dfs(person):
			for idx, tmp in enumerate(M[person]):
				if tmp and idx not in visited:
					visited.add(idx)
					dfs(idx)

		for i in range(people):
			if i not in visited:
				res += 1
				dfs(i)
		return res

	def findCircleNum1(self, M):
		f = {}
		n = len(M)
		def find(x):
			f.setdefault(x,x)
			if x != f[x]:
				f[x] = find(f[x])
			return f[x]
		def union(x,y):
			f[find(y)] = find(x)

		for i in range(n):
			for j in range(i,n):
				if M[i][j] == 1:
					union(i,j)
		print(f)
		return len(set(map(find, f)))




a = Solution()
print(a.findCircleNum1([[1, 1, 0],
					   [1, 1, 0],
					   [0, 0, 1]]))
