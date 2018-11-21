class Solution(object):
	def fractionAddition(self, expression):
		"""
		给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。 这个结果应该是不可约分的分数，即最简分数。
		如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
		---
		输入:"-1/2+1/2"
		输出: "0/1"
		---
		输入:"-1/2+1/2+1/3"
		输出: "1/3"
		---
		输入:"1/3-1/2"
		输出: "-1/6"
		:type expression: str
		:rtype: str
		"""
		nums = []
		n = len(expression)
		i = 0
		# 把所有分数找出来
		while i < n :
			# print(i)
			if expression[i] == "-":
				temp = i
				i += 1
				while i < n and expression[i] != "+" and expression[i] !="-":
					i += 1
				nums.append(expression[temp:i])
			else:
				temp = i
				i += 1
				while i < n and expression[i] != "+" and expression[i] !="-":
					i += 1
				nums.append(expression[temp:i])
		# print(nums)
		# 把所有分数拆成分子和分母
		res = []
		for num in nums:
			num = num.split("/")
			res.append([int(num[0]),int(num[-1])])
		# print(res)
		# 所有分母相乘，找到共同分母
		max_gong = 1
		for i in res:
			max_gong *= i[1]
		# 使相应的分子也扩大同样的倍数
		l = len(res)
		j = 0
		while j < l:
			# res[j][1] = max_gong
			res[j][0] = (max_gong//res[j][1])* res[j][0]
			res[j][1] = max_gong
			j += 1
		# 分子进行相应的运算
		fenzi = sum(map(lambda x:x[0],res))
		# print(fenzi,max_gong)
		if fenzi == 0:
			return "0/1"
		if fenzi % max_gong == 0:
			return str(fenzi//max_gong)+"/1"
		# 找分子，分母的最大公约数
		def GCU(m,n):
			while m%n:
				m,n = n,m%n
			return n
		gcu = GCU(int(fenzi),int(max_gong))
		# print(gcu)
		return str(fenzi//gcu) + "/" + str(max_gong//gcu)


a = Solution()
print(a.fractionAddition("-1/2+1/2"))
print(a.fractionAddition("-1/2+1/2+1/3"))
print(a.fractionAddition("1/3-1/2"))
