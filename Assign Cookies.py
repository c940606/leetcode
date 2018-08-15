class Solution:
	def findContentChildren(self, g, s):
		"""
		假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
		对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，
		都有一个尺寸 sj 。如果 sj >= gi ，
		我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
		---
		输入: [1,2,3], [1,1]
		输出: 1
		解释:
		你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
		虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
		所以你应该输出1。
		---
		思路：
		小孩，饼干 先从小到大排序
		一次选取小孩，
		1. 小孩满足感 ，找到饼干里最少
		:type g: List[int]
		:type s: List[int]
		:rtype: int
		"""
		g.sort()
		s.sort()
		n = len(g)
		m = len(s)
		i,j = 0,0
		count = 0
		while i<n and j<m:
			while j<m and g[i] > s[j] :
				j += 1
			if j < m:
				i += 1
				j += 1
				count += 1
		return count
a = Solution()
print(a.findContentChildren([1,2], [1,2,3]))

