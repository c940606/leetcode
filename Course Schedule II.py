class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		from collections import defaultdict
		if not prerequisites:
			return list(range(numCourses))
		graph = defaultdict(list)
		for x, y in prerequisites:
			graph[x].append(y)

		visited = set()
		being_visited = set()
		res = []

		def dfs(course):
			if course in being_visited:
				return False
			if course in visited:
				return True
			visited.add(course)
			being_visited.add(course)
			for tmp in graph[course]:
				if not dfs(tmp):
					return False
			being_visited.remove(course)
			res.append(course)
			return True

		for course in range(numCourses):
			if not dfs(course):
				return []
		return res[::-1]

	def findOrder1(self, numCourses, prerequisites):
		from collections import deque, defaultdict
		in_degree = [0] * numCourses
		graph = defaultdict(list)
		for x, y in prerequisites:
			in_degree[y] += 1
			graph[x].append(y)

		queue = deque()
		for i in range(numCourses):
			if in_degree[i] == 0:
				queue.appendleft(i)
		res = []
		# print(queue)
		while queue:
			tmp = queue.pop()
			res.append(tmp)
			for tmp_course in graph[tmp]:
				in_degree[tmp_course] -= 1
				if in_degree[tmp_course] == 0:
					queue.appendleft(tmp_course)
		return res


a = Solution()
# print(a.findOrder1(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# print(a.findOrder1(2, [[1, 0]]))
# print(a.findOrder1(2, [[0, 1]]))
print(a.findOrder1(3, [[1, 0]]))
