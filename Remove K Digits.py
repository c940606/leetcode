class Solution(object):
	def removeKdigits(self, num, k):
		"""
		给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
		注意:
			num 的长度小于 10002 且 ≥ k。
			num 不会包含任何前导零。
		---
		输入: num = "1432219", k = 3
		输出: "1219"
		解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
		---
		思路：
		暴力求解
		:type num: str
		:type k: int
		:rtype: str
		"""
		if k >= len(num):
			return 0
		self.min_num = "100000"

		self.force(num,k)
		return self.min_num

	def force(self,num, k):
		# if not num :
		# 	self.min_num = 0
		# 	return
		if k == 0:
			# print(num)
			# print(self.min_num)
			if int(self.min_num) > int(num):
				# print(num)
				self.min_num = (num)
			else:
				return
		for i in range(len(num)):
			self.force(num[:i] + num[i + 1:], k - 1)

	def removeKdigits1(self, num, k):
		res = []
		for i in range(len(num)):
			while k and res and res[-1] > num[i]:
				res.pop()
				k -= 1
			if  res or num[i] != "0":
				res.append(num[i])
		res = res[:len(res)-k]
		if not res:
			return "0"
		return "".join(res)


		# stack = []
		# remaining = []
		# # s = k
		# n = len(num)
		# if k == n:
		# 	return "0"
		# for i in range(n):
		# 	# if i == k+len(stack):
		# 	# 	stack.extend(num[i:])
		# 	# 	break
		# 	# if len(stack) == n - k and stack[-1]>num[i]:
		# 	# 	stack.pop()
		# 	# 	stack.append(num[i])
		# 	# 	break
		# 	# if len(stack) == n-k:
		# 	# 	break
		# 	# if k == 0:
		# 	# 	break
		#
		# 	if not stack:
		# 		stack.append(num[i])
		# 		continue
		# 	if int(stack[-1]) > int(num[i]):
		# 		stack.pop()
		# 		k -= 1
		# 	stack.append(num[i])




		# print(stack)
		# return str(int("".join(stack)))




a = Solution()
print(a.removeKdigits1(num = "10", k = 2))
print(a.removeKdigits1(num = "1432219", k = 3))
print(a.removeKdigits1(num = "10200", k = 1))
print(a.removeKdigits1(num = "112", k = 1))
# print(a.removeKdigits1(num = "12", k = 1))
# print(a.removeKdigits1(num = "1234567890", k = 9))
#
#
print(a.removeKdigits1(num = "9999999999991", k = 8))

