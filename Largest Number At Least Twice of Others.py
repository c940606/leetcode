class Solution(object):
	def dominantIndex(self, nums):
		"""
		在一个给定的数组nums中，总是存在一个最大元素 。
		查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
		如果是，则返回最大元素的索引，否则返回-1。
		---
		输入: nums = [3, 6, 1, 0]
		输出: 1
		解释: 6是最大的整数, 对于数组中的其他整数,
		6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
		---
		输入: nums = [1, 2, 3, 4]
		输出: -1
		解释: 4没有超过3的两倍大, 所以我们返回 -1.
		---
		思路:
		找到最大元素 去除
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return -1
		max_num = max(nums)
		idx = nums.index(max_num)

		nums.remove(max_num)
		# print(nums)
		if all(map(lambda x:True if x*2 <= max_num else False,nums)):
			return idx
		return -1
a = Solution()
print(a.dominantIndex([3, 6, 1, 0]))
