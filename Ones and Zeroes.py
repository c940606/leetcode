class Solution(object):
	def findMaxForm(self, strs, m, n):
		"""
		在计算机界中，我们总是追求用有限的资源获取最大的收益。
		现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
		你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
		注意:
		给定 0 和 1 的数量都不会超过 100。
		给定字符串数组的长度不会超过 600。
		---
		示例 1:
		输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
		输出: 4
		解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
		---
		示例 2:
		输入: Array = {"10", "0", "1"}, m = 1, n = 1
		输出: 2
		解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""
		if not strs:
			return 0
		nums = len(strs)
		dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(nums + 1)]
		# print(dp)
		for i in range(1, nums + 1):
			temp_n = len(strs[i - 1])
			zero_nums = strs[i - 1].count("0")
			one_nums = temp_n - zero_nums
			# print(zero_nums,one_nums)
			for j in range(m+1):
				for k in range(n+1):
					# print(i,k)
					# print(zero_nums,one_nums)
					if j >= zero_nums and k >= one_nums:
						dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero_nums][k - one_nums] + 1)
					else:
						dp[i][j][k] = dp[i - 1][j][k]
					# print(dp)
		return dp[-1][-1][-1]

	def findMaxForm1(self, strs, m, n):
		if not strs:
			return 0
		nums = len(strs)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(nums):
			# 先计算有多少0和1
			zero_nums = 0
			one_nums = 0
			for alp in strs[i]:
				if alp == "0":
					zero_nums += 1
				else:
					one_nums += 1
			for j in range(m,-1,-1):
				for k in range(n,-1,-1):
					if j >= zero_nums and k >= one_nums:
						dp[j][k] = max(dp[j][k],dp[j-zero_nums][k-one_nums]+1)
		# print(dp)
		return dp[-1][-1]


a = Solution()
print(a.findMaxForm(["10", "0001", "111001", "1", "0"], m=5, n=3))
print(a.findMaxForm1(["10", "0001", "111001", "1", "0"], m=5, n=3))
# print(a.findMaxForm(["10", "0", "1"], m=1, n=1))
# print(a.findMaxForm(["110110001001100","0000011"],19,1))
