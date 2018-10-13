class Solution(object):
	def selfDividingNumbers(self, left, right):
		"""
		自除数 是指可以被它包含的每一位数除尽的数。
		例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
		还有，自除数不允许包含 0 。
		给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
		---
		输入：
		上边界left = 1, 下边界right = 22
		输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		res = []
		for num in range(left,right+1):
			if all(map(lambda x:num%int(x)==0 if int(x) != 0 else False,str(num))):
				res.append(num)
		return res
a = Solution()
print(a.selfDividingNumbers(1,22))
