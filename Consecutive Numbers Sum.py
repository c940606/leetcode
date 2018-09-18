class Solution(object):
	def consecutiveNumbersSum(self, N):
		"""
		给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
		---
		输入: 5
		输出: 2
		解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
		--
		思路:
		用求和公式
		(an-a1+1)(an+a1) = 2N
		:type N: int
		:rtype: int
		"""
		x = 2*N
		l = int(x**0.5)
		print(l)
		num = 1
		temp =[]
		for i in  range(2,l+1):
			print(i)
			if x % i == 0:
				an = 0.5*(x/i+i-1)
				a1 = x/i - an
				print(a1,an)
				if an > a1 and int(an) == an and int(a1) ==a1:
					if (an-a1+1)*(an+a1)==x:
						num += 1
						temp.append([int(a1),int(an)])
		temp.append([N])
		return num,temp
a = Solution()
print(a.consecutiveNumbersSum(15))

