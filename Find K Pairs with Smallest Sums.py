class Solution(object):
	def kSmallestPairs(self, nums1, nums2, k):
		"""
		给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
		定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
		找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。
		---
		给出： nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
		返回： [1,2],[1,4],[1,6]
		返回序列中的前 3 对数：
		[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
		---
		给出：nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
		返回： [1,1],[1,1]
		返回序列中的前 2 对数：
		[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
		---
		给出：nums1 = [1,2], nums2 = [3],  k = 3
		返回： [1,3],[2,3]
		也可能序列中所有的数对都被返回:
		[1,3],[2,3]
		---
		思路：
		1. 如果k比他所有还有大 ，就是返回所有排序
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[List[int]]
		"""
		n1 = len(nums1)
		n2 = len(nums2)
		res = []
		if k > n1*n2:
			for i in range(n1):
				for j in range(n2):
					res.append([nums1[i],nums2[j]])
			return ",".join(map(str,res))
		else:

			for i in range(n1):
				for j in range(n2):
					if k > 0:
						res.append([nums1[i], nums2[j]])
						k -= 1
					else:
						break
			return ",".join(map(str, res))

a = Solution()
print(a.kSmallestPairs([1,7,11],[2,4,6],3))
