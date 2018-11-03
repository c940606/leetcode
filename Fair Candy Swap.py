class Solution(object):
	def fairCandySwap(self, A, B):
		"""
		爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。
		因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。
		（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
		返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
		如果有多个答案，你可以返回其中任何一个。保证答案存在。
		---
		1 <= A.length <= 10000
		1 <= B.length <= 10000
		1 <= A[i] <= 100000
		1 <= B[i] <= 100000
		保证爱丽丝与鲍勃的糖果总量不同。
		答案肯定存在。
		:type A: List[int]
		:type B: List[int]
		:rtype: List[int]
		"""
		sum_A = sum(A)
		sum_B = sum(B)
		avg = (sum_A+sum_B)/2
		flag = int(sum_A - avg)
		A = set(A)
		B = set(B)
		print(flag)
		if flag > 0:
			for num in A:
				if num-flag in B:
					return [num,num-flag]
		else:
			for num in B:
				if num -abs(flag) in A:
					return [num-abs(flag),num]
a = Solution()
print(a.fairCandySwap(A = [1,1], B = [2,2]))
print(a.fairCandySwap(A = [1,2], B = [2,3]))
print(a.fairCandySwap(A = [2], B = [1,3]))
print(a.fairCandySwap(A = [1,2,5], B = [2,4]))
