class Solution:
	def plusOne(self, digits):
		"""
		给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
		最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
		你可以假设除了整数 0 之外，这个整数不会以零开头。
		----
		输入: [1,2,3]
		输出: [1,2,4]
		解释: 输入数组表示数字 123。
		:type digits: List[int]
		:rtype: List[int]
		"""
		num = int("".join(map(str,digits)))+1
		return list(map(int,str(num)))
a = Solution()
obj = [1,2,3]
print(a.plusOne(obj))