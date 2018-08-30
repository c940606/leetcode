from collections import Counter
class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
		---
		输入: nums = [1,1,1,2,2,3], k = 2
		输出: [1,2]
		---
		思路：
		字典
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		c = Counter(nums)
		c = sorted(c.items(),key= lambda x:x[1],reverse=True)
		print(c)
		c = list(map(lambda x:x[0],c))
		return c[:k]
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3],2))

