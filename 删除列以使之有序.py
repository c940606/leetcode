class Solution(object):
	def minDeletionSize(self, A):
		"""
		:type A: List[str]
		:rtype: int
		"""
		lookup = [chr(i) for i in range(97,123)]
		# print(lookup)
		A = [list(i) for i in A]
		# print(A)
		count = 0
		def jugle_sort(col):
			# print(col == sorted(col))
			return list(col) == sorted(col)
		for col in zip(*A):
			if not jugle_sort(col):
				print(col)
				count += 1
		return count

a = Solution()
print(a.minDeletionSize(["cba","daf","ghi"]))
print(a.minDeletionSize(["zyx","wvu","tsr"]))
