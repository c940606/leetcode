class Solution(object):
	def multiply(self, num1, num2):
		"""
		给定两个以字符串形式表示的非负整数 num1 和 num2，
		返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
		---
		输入: num1 = "2", num2 = "3"
		输出: "6"
		---
		输入: num1 = "123", num2 = "456"
		输出: "56088"
		---
		思路:
		用乘法公式
		1. 相乘的位数最大是6位
		2. 先用一个数组 表示个个数相乘记录
		3. 超过10，向前进位
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if num1 == "0" or num2 == "0":
			return "0"
		lookup = {"0":0,
				  "1":1,
				  "2":2,
				  "3":3,
				  "4":4,
				  "5":5,
				  "6":6,
				  "7":7,
				  "8":8,
				  "9":9
				  }
		n1 = len(num1)
		n2 = len(num2)
		# print(n1+n2)
		temp = [0]*(n1+n2)
		# print(temp)
		f = 0
		num1 = num1[::-1]
		num2 = num2[::-1]
		for i in num1:
			k = 0
			for j in num2:
				temp[f+k] += lookup[i]*lookup[j]
				k += 1
			f += 1
		# print(temp)
		# res = [0]*(n1+n2)
		i = 0
		while True:
			q, r = divmod(temp[i], 10)
			if i < n1+n2-1:
				temp[i] = r
				temp[i+1] += q
				i += 1
			else:
				temp[i] =r
				break
		temp = temp[::-1]
		return "".join(map(str,temp)).lstrip("0")






a = Solution()
print(a.multiply("123","456"))

