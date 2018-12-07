class Solution:
	def combinationSum(self, candidates, target):
		"""
		给定一个无重复元素的数组 candidates 和一个目标数 target ，
		找出 candidates 中所有可以使数字和为 target 的组合。
		candidates 中的数字可以无限制重复被选取。
		-----------------------------
		输入: candidates = [2,3,6,7], target = 7,
			所求解集为:
			[
			  [7],
			  [2,2,3]
			]
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates.sort()
		self.res = []
		self.combination([],candidates,target)
		return self.res


	def combination(self,sing_list,candidates,target):
		if target == 0:
			sing_list.sort()
			if sing_list not in self.res:
				self.res.append(sing_list)
		if target > 0:
			for num in candidates:
					self.combination(sing_list+[num],candidates,target-num)
		# else:
		# 	sing_list = []

	def combinationSum1(self, candidates, target):
		if not candidates:
			return []
		if min(candidates) > target:
			return []
		candidates.sort()
		res = []

		def helper(candidates, target, temp_list):
			if target == 0:
				res.append(temp_list)
			if target < 0:
				return
			for i in range(len(candidates)):
				if candidates[i] > target:
					continue
				helper(candidates[i:], target - candidates[i], temp_list + [candidates[i]])
		helper(candidates,target,[])
		return res

candidates = [2,3,6,7]
target = 7
a = Solution()
print(a.combinationSum1(candidates,target))

