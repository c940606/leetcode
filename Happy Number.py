class Solution:
	def isHappy(self, n):
		"""
		编写一个算法来判断一个数是不是“快乐数”。
		一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
		然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数
		:type n: int
		:rtype: bool
		"""
		num = self.Sum(n)
		# print("----")
		# print(num)
		if num == 1:
			return True
		if num == 4:
			return False
		else:
			return self.isHappy(num)

	def Sum(self, n):
		num_list = map(int,str(n))
		# print(num_list)
		all_Sum = 0
		for num in num_list:
			all_Sum += (num*num)
		# print(Sum)
		return all_Sum
a = Solution()

for i in range(1,50000):
	if a.isHappy(i):
		print(i)