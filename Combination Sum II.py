class Solution:
	def combinationSum2(self, candidates, target):
		"""
		给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
		candidates 中的每个数字在每个组合中只能使用一次。
		--------------
		输入: candidates = [10,1,2,7,6,1,5], target = 8,
			所求解集为:
			[
			  [1, 7],
			  [1, 2, 5],
			  [2, 6],
			  [1, 1, 6]
			]
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates.sort()
		self.res = []
		self.dfs([],candidates,target)
		return self.res
	def dfs(self,sing_list,candidates,target):
		if target == 0:
			sing_list.sort()
			if  sing_list not in self.res:
				self.res.append(sing_list)
		if target > 0 and candidates:
			for i in range(len(candidates)):
				if candidates[i]>target:
					break
				else:
					self.dfs(sing_list+[candidates[i]],candidates[i+1:],target-candidates[i])
		# else:
		# 	break

	def combinationSum(self, candidates, target):
		if not candidates:
			return []
		if min(candidates) > target:
			return []
		res = []
		n = len(candidates)
		candidates.sort()
		def helper(idx, temp_list, target):
			if target == 0:
				res.append(temp_list)
			if target < 0:
				return
			for i in range(idx, n):
				# print(i)
				if i > idx and candidates[i-1] == candidates[i]:
					continue
				if candidates[i] > target:
					break
				helper(i + 1, temp_list + [candidates[i]], target - candidates[i])
		helper(0,[],target)
		return res

a = Solution()
candidates1 = [10,1,2,7,6,1,5]
target1 = 8
candidates2 = [1,2]
target2 = 4
print(a.combinationSum(candidates1,target1))
