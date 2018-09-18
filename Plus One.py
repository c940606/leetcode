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

	def plusOne1(self, digits):
		n = len(digits)
		flag = 1
		i = n-1
		while True:
			if i == -1:
				digits.insert(0,1)
				break
			temp = digits[i] + flag
			flag = temp // 10
			digits[i] = temp % 10
			if flag == 0:
				break
			else:
				i -= 1
		return digits



a = Solution()
obj = [9,9,9,9]
print(a.plusOne1(obj))