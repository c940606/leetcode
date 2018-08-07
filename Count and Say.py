class Solution:
	def countAndSay(self, n):
		"""
		报数序列是指一个整数序列，按照其中的整数的顺序进行报数，
		得到下一个数。其前五项如下：
		1.     1
		2.     11
		3.     21
		4.     1211
		5.     111221
		1 被读作  "one 1"  ("一个一") , 即 11。
		11 被读作 "two 1s" ("两个一"）, 即 21。
		21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
		给定一个正整数 n ，输出报数序列的第 n 项。
		注意：整数顺序将表示为一个字符串。
		------------
		输入: 1
		输出: "1"
		:type n: int
		:rtype: str
		"""

		temp = "1"
		count = 1
		while count < n:
			temp = self.neXt(temp)
			count += 1
		return temp


	def neXt(self,num):
		s = str(num)
		res = ""
		i = 0
		while i < len(s):
			if i == len(s)-1:
				res += ("1"+s[i])
				break
			count =1
			while i< len(s)-1 and s[i] == s[i+1]:
				count += 1
				i += 1
			# if i == len(s)-1:
			# 	count += 0
			temp = str(count)+s[i]
			res += temp
			i += 1
		return res

	def countAndSay2(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		if n == 1:
			return '1'
		s = self.countAndSay2(n - 1) + '*'
		res, count = '', 1
		for i in range(len(s) - 1):
			if s[i] == s[i + 1]:
				count += 1
			else:
				res += str(count) + str(s[i])
				count = 1
		return res

	def countAndSay3(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		index = 1
		string = '1'
		while index < n:
			num = 0
			nextStr = ''
			prech = string[0]
			for ch in string:
				if ch == prech:
					num += 1
				else:
					nextStr += (str(num) + prech)
					num = 1
					prech = ch
			nextStr += (str(num) + prech)
			string = nextStr
			index += 1
		return string
a = Solution()
print("--->1",a.countAndSay(45))
# print("---")
print("--->2",a.countAndSay2(45))
# print("---")
print("--->3",a.countAndSay3(45))