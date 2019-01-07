class Solution(object):
	def reorderLogFiles(self, logs):
		"""
		:type logs: List[str]
		:rtype: List[str]
		"""
		if not logs:
			return []
		res1 = []
		res2= []
		for log in logs:
			if  log.split(" ")[1].isdigit():
				res2.append(log)
			else:
				res1.append(log)
		res1 = (sorted(res1,key=lambda x:x.split()[1:]))
		return res1 + res2
a = Solution()
print(a.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act aoo"]))
