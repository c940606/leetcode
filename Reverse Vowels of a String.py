class Solution:
	def reverseVowels(self, s):
		"""
		编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
		---
		输入: "hello"
		输出: "holle"
		---
		思路：
		用首尾指针，当同时遇到元音字母交换
		:type s: str
		:rtype: str
		"""
		y_alp = ["a","o","e","i","u","A","O","E","I","U"]
		s_list= list(s)
		n = len(s)

		i = 0
		j = n-1
		while i<j:

			while i < n and s_list[i] not in y_alp:
				i += 1
			# print(i)
			while j> 0 and s_list[j] not in y_alp:
				j -= 1
			if i >= j :
				break
			# print(j)
			s_list[i],s_list[j] = s_list[j],s_list[i]
			# print(s)
			i += 1
			j -= 1
		return "".join(s_list)
a = Solution()
s= "hello"
print(a.reverseVowels(s))
