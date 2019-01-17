class Solution(object):
	def fourSumCount(self, A, B, C, D):
		"""
		给定四个包含整数的数组列表 A , B , C , D ,
		计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
		为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
		所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
		---
		输入:
		A = [ 1, 2]
		B = [-2,-1]
		C = [-1, 2]
		D = [ 0, 2]
		输出:
		2
		解释:
		两个元组如下:
		1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
		2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
		---
		思路:

		:type A: List[int]
		:type B: List[int]
		:type C: List[int]
		:type D: List[int]
		:rtype: int
		"""
		n = len(A)
		res = []
		for i in range(n):
			for j in range(n):
				for k in range(n):
					for s in range(n):
						if A[i] + B[j] + C[k] + D[s] == 0:
							res.append((i,j,k,s))
		return res

	def fourSumCount1(self, A, B, C, D):
		"""
		思路:
		哈希表+二次查找
		哈希表 第一要表示 来自哪个矩阵
			  第二要表示  来自的索引号
		:param A:
		:param B:
		:param C:
		:param D:
		:return:
		"""
		# print(A)
		if not A:
			return 0
		lookup_A = []
		lookup_B = []
		lookup_C = []
		lookup_D = []
		for idx,num in enumerate(A):
			lookup_A.append((num,"A",idx))
		for idx,num in enumerate(B):
			lookup_B.append((num,"B",idx))
		for idx,num in enumerate(C):
			lookup_C.append((num,"C",idx))
		for idx,num in enumerate(D):
			lookup_D.append((num,"D",idx))
		comall = lookup_A+lookup_B+lookup_C+lookup_D
		comall = sorted(comall,key = lambda x:x[0])
		# print(comall)
		# flag = []
		n = len(comall)
		res = []
		count = 0
		target = 0
		print(comall)
		for i in range(n-3):
			# if i > 0 and comall[i][0] == comall[i-1][0]:
				# continue
			if comall[i][0]+comall[i+1][0]+comall[i+2][0]+comall[i+3][0] > target:
				break
			if comall[i][0] + comall[-1][0]+comall[-2][0]+comall[-3][0] < target:
				continue
			for j in range(i+1,n-2):
				# if comall[j][0] == comall[j-1][0]:
					# continue
				# print(i,j)
				if comall[i][0] + comall[j][0] + comall[j+1][0] + comall[j+2][0] > target:
					break
				if comall[i][0] + comall[j][0] + comall[-1][0] + comall[-2][0] < target:
					continue
				left = j + 1
				right = n - 1
				# print(comall)
				while left < right:
					temp = comall[i][0] + comall[j][0] + comall[left][0] + comall[right][0]
					# print(temp)
					if  temp == target:
						print(i,j,left,right)
						# res.append([comall[i],comall[j],comall[left],comall[right]])
						temp_left = left
						temp_right = right
						while left < right and comall[left][0] == comall[left+1][0]:
							# res.append([comall[i],comall[j],comall[left+1],comall[right]])
							left += 1
						while temp_left < right and comall[right][0] == comall[right-1][0]:
							print("..")
							# res.append([comall[i],comall[j],comall[left+1],comall[right-1]])
							right -= 1
						print(left,right)
						for s in range(temp_left,left+1):
							for k in range(right,temp_right+1):

								if s >= k:
									continue
								# print(i, j, s, k)
								# res.append([comall[i],comall[j],comall[s],comall[k]])
								flag = []
								for item in [comall[i],comall[j],comall[s],comall[k]]:
									if item[1] in flag:
										break
									flag.append(item[1])
									if len(flag) == 4:
										count += 1
										res.append([comall[i], comall[j], comall[s], comall[k]])
						left += 1
						right -= 1
					elif temp < target:
						left += 1
					else:
						right -= 1
		# print(res)
		# # print("---")
		# result = []
		# count = 0
		# for tup in res:
		# 	flag = []
		# 	# print(tup)
		# 	for item in tup:
		# 		# print(item)
		# 		if item[1] in flag:
		# 			break
		# 		flag.append(item[1])
		# 	if len(flag) == 4:
		# 		result.append(tup)
		# 		count += 1
		print(res)
		return count




a = Solution()
# print(a.fourSumCount1(A = [ 1, 2],B = [-2,-1],C = [-1, 2],D = [ 0, 2]))
print(a.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1]))
