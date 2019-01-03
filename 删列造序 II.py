class Solution(object):
	def minDeletionSize(self, A):
		"""
		:type A: List[str]
		:rtype: int
		"""
		if not A:
			return 0
		res = 0
		n = len(A)
		cur = [""] * n
		for col in zip(*A):
			tmp = list(map(lambda i:cur[i] + col[i],range(n)))
			# print(tmp)
			if sorted(tmp) ==  tmp :
				cur = tmp
			else:
				res += 1
		return res

a = Solution()
print(a.minDeletionSize(["ca","bb","ac"]))
# print(a.minDeletionSize(["xc","yb","za"]))
# print(a.minDeletionSize(["zyx","wvu","tsr"]))
# print(a.minDeletionSize(["xga","xfb","yfa"]))