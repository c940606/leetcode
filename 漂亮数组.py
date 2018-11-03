class Solution(object):
	def beautifulArray(self, N):
		"""
		对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：
		对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。
		那么数组 A 是漂亮数组。
		给定 N，返回任意漂亮数组 A（保证存在一个）。
		--
		输入：4
		输出：[2,1,4,3]
		:type N: int
		:rtype: List[int]
		"""
		if N == 1:
			return [1]
		a = [x*2-1 for x in self.beautifulArray((N+1)//2)]
		print(a)
		b = [x*2 for x in self.beautifulArray(N//2)]
		print(b)
		r = a + b
		print(r)
		print("-----")
		return r
a = Solution()
print(a.beautifulArray(4))


