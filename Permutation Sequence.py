class Solution:
	def getPermutation(self, n, k):
		"""
		给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

		按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

		"123"
		"132"
		"213"
		"231"
		"312"
		"321"
		给定 n 和 k，返回第 k 个排列。
		----------
		输入: n = 3, k = 3
		输出: "213"
		:type n: int
		:type k: int
		:rtype: str
		"""
		self.res = []
		nums = [str(i+1) for i in range(n)]
		self.dft("", nums,k,n)
		print(self.res)
		return int(self.res[-1])

	def dft(self, sing_list,nums,k,n):
		if n == 0 :
			self.res.append(sing_list)
		if len(self.res) < k:
			for i in range(len(nums)):
				self.dft(sing_list + nums[i], nums[0:i] + nums[i + 1:],k, n - 1)
a = Solution()
print(a.getPermutation(3,3))