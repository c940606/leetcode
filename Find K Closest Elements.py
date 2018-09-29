class Solution(object):
	def findClosestElements(self, arr, k, x):
		"""
		给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。
		返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
		---
		输入: [1,2,3,4,5], k=4, x=3
		输出: [1,2,3,4]
		---
		输入: [1,2,3,4,5], k=4, x=-1
		输出: [1,2,3,4]
		---
		思路:
		先找到最靠近 x 的值 --- 二分法
		如果在0 位置 return arr[:k]
		如果在 n 位置 return arr[-k:]
		其他位置
			i = mid
			j = mid
			while i >= 0 and abc(mid - i) <= abc[mid - j]:
					i -= 1
			while j < n and abc(mid-j)< abc(mid-j):
				j +=1
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""
		if not arr:
			return
		n = len(arr)
		def look_x (arr):

			i = 0
			j = n-1
			while i<=j:
				mid = (i+j)//2
				if arr[mid] == x:
					return mid
				elif arr[mid] > x:
					j = mid-1
				else:
					i = mid + 1
			return mid

		ide = look_x(arr)
		print(ide)
		if ide == 0:
			return arr[:k]
		if ide == n-1:
			return arr[-k:]
		left_res = []
		right_res = []
		left = ide
		right = ide+1
		count = 0
		while count < k:
			# print(left,right)
			if left < 0:
				break
			if right >=n:
				break
			while left >=0 and count < k and abs(arr[left]-x)<=abs(arr[right]-x):
				left_res.append(arr[left])
				left -= 1
				count += 1
			while right < n and count < k and abs(arr[right]-x) < abs(arr[left]-x):
				right_res.append(arr[right])
				right += 1
				count += 1
		print(left,right)
		if right==n:
			while count < k:
				left_res.append(arr[left])
				left -=1
				count += 1
		if left == 0:
			while count < k:
				right_res.append(arr[right])
				right += 1
				count += 1
		print(left_res,right_res)
		return left_res[::-1]+right_res


a = Solution()
print(a.findClosestElements([1,2,3,4,5],4,3))



