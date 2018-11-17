class Solution(object):
	def reconstructQueue(self, people):
		"""
		假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，
		其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
		注意：
		总人数少于1100人。
		---
		输入:
		[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
		输出:
		[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		from functools import cmp_to_key
		if not people:
			return []
		# people = sorted(people,key=cmp_to_key(lambda x,y: y[0]-x[0] if x[0] != y[0] else x[1]-y[1]))
		# people = sorted(people,key=lambda x:x[1])
		people = sorted(people,key=lambda x:(x[0],-x[1]),reverse=True)
		print(people)
		res=[]
		for p in people:
			res.insert(p[1],p)
			print(res)
		return res
a = Solution()
print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
