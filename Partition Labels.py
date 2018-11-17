class Solution(object):
	def partitionLabels(self, S):
		"""
		字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
		同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
		--
		输入: S = "ababcbacadefegdehijhklij"
		输出: [9,7,8]
		解释:
		划分结果为 "ababcbaca", "defegde", "hijhklij"。
		每个字母最多出现在一个片段中。
		像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
		--

		:type S: str
		:rtype: List[int]
		"""
		if not S:
			return []
		def helper(a_str):
			left = 0
			right = a_str.rfind(a_str[left])
			while left < right:
				left += 1
				temp = a_str.rfind(a_str[left])
				if temp > right:
					right = temp
			return right
		res = []
		while S:
			loc = helper(S)
			res.append(loc+1)
			S = S[loc+1:]
		return res

	def partitionLabels1(self, S):
		lookup = {}
		n = len(S)
		for i in range(n):
			lookup[S[i]] = i
		last = 0
		start = -1
		res = []
		for i in range(n):
			if lookup[S[i]] > last:
				last = lookup[S[i]]
			if i == last:
				res.append(last-start)
				start = last
		return res
a = Solution()
print(a.partitionLabels1(S = "ababcbacadefegdehijhklij"))
