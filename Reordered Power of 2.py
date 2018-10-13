class Solution(object):
	def reorderedPowerOf2(self, N):
		"""
		从正整数 N 开始，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
		如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
		:type N: int
		:rtype: bool
		"""
		N = str(N)
		res = []
		n = len(N)
		def helper(temp,N):
			if not N and len(str(int(temp))) == n:
				res.append(int(temp))
			for i in range(len(N)):
				helper(temp+N[i],N[:i]+N[i+1:])
		helper("",N)
		print(res)
		for num in res:
			if bin(num).count("1") == 1:
				return True
		return False
a = Solution()
print(a.reorderedPowerOf2(14806876))
