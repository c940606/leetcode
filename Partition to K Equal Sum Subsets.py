class Solution(object):
	def canPartitionKSubsets(self, nums, k):
		"""
		给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
		---
		示例 1：
		输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
		输出： True
		说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
		---
		注意:
		1 <= k <= len(nums) <= 16
		0 < nums[i] < 10000
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		sum_nums = sum(nums)
		avg = sum_nums // k
		if k <= 0 or sum_nums % k != 0 or max(nums) > avg:
			return False
		n = len(nums)
		visited = [0] * n
		nums = sorted(nums, reverse=True)
		return self.canPartition(nums, visited, 0, k, 0, 0, avg)

	def canPartition(self, nums, visited, start_index, k, cur_sum, cur_num, target):
		if k == 1:
			return True
		if cur_sum == target and cur_num > 0:
			return self.canPartition(nums, visited, 0, k - 1, 0, 0, target)
		if cur_sum > target:
			return False
		for i in range(start_index, len(nums)):
			if visited[i] == 0:
				visited[i] = 1
				if self.canPartition(nums, visited, i + 1, k, cur_sum + nums[i], cur_num + 1, target):
					return True
				visited[i] = 0
		return False


a = Solution()
print(a.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
