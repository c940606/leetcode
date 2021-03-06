class Solution(object):
	def fourSumCount(self, A, B, C, D):
		"""
		给定四个包含整数的数组列表 A , B , C , D ,
		计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
		为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
		所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
		---
		:type A: List[int]
		:type B: List[int]
		:type C: List[int]
		:type D: List[int]
		:rtype: int
		"""
