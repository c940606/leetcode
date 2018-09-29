class Solution(object):
	def smallestRangeI(self, A, K):
		"""
		给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。
		在此过程之后，我们得到一些数组 B。
		返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
		---
		输入：A = [1], K = 0
		输出：0
		解释：B = [1]
		---
		输入：A = [0,10], K = 2
		输出：6
		解释：B = [2,8]
		:type A: List[int]
		:type K: int
		:rtype: int
		"""
		n = len(A)
		if n == 1:
			return 0
		max_num = max(A)
		while max_num in A:
			A.remove(max_num)
		max2_num = max(A)
		if max_num - max2_num <= 2*K:
			return 0
		return max_num-max2_num-2*K

a = Solution()
print(a.smallestRangeI([0,10],2))