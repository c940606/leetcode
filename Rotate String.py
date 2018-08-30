class Solution(object):
	def rotateString(self, A, B):
		"""
		给定两个字符串, A 和 B。
		A 的旋转操作就是将 A 最左边的字符移动到最右边。
		例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
		如果在若干次旋转操作之后，A 能变成B，那么返回True。
		---
		示例 1:
		输入: A = 'abcde', B = 'cdeab'
		输出: true

		示例 2:
		输入: A = 'abcde', B = 'abced'
		输出: false
		---
		思路:
		1. 看长度是否一样
		2.
		:type A: str
		:type B: str
		:rtype: bool
		"""
		n = len(A)
		m = len(B)
		if n != m:
			return False
		i = 0
		while i < n:
			if A[i:]+A[:i] == B:
				return True
			i += 1
		return False
a = Solution()
print(a.rotateString(A = 'abcde', B = 'abced'))
