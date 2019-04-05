class Solution(object):
	def maxChunksToSorted(self, arr):
		"""
		数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，
		并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
		我们最多能将数组分成多少块？
		---
		输入: arr = [4,3,2,1,0]
		输出: 1
		解释:
		将数组分成2块或者更多块，都无法得到所需的结果。
		例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
		---
		输入: arr = [1,0,2,3,4]
		输出: 4
		解释:
		我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
		然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
		----
		思路:
		跳转 一个指针 如果相等 一个划分
		            小于 检查前面 是否有大于 次位置标号 如果有 移动当前位置 没有 可以做一次划分
		            大于 当前位置 移动 大于这个位置
		:type arr: List[int]
		:rtype: int
		"""
		n = len(arr)
		begin = 0
		p = 0
		count = 0
		while p < n :
			print(p)
			if arr[p] == p:
				print("""one""")
				count += 1
				p += 1
				begin = p
			elif arr[p] > p:
				print("two")
				# print(arr[p])
				p = arr[p]
			else:
				print("three")
				max_num = max(arr[begin:p+1])
				if max_num == p:
					count += 1
					p += 1
					begin = p
				else:
					p = max_num
			print(begin,p)
		return count

	def maxChunksToSorted1(self, arr):
		maxn = 0
		n = len(arr)
		count = 0
		for i in range(n):
			maxn = max(maxn, arr[i])
			if maxn == i:
				count +=1
		return count
	def maxChunksToSorted2(self,arr):
		n = len(arr)
		right = 0
		left = 0
		res = 0
		while right < n:
			right = arr[left]
			while left < n and left < right:
				left += 1
				right = max(arr[left],right)
			res += 1
			right += 1
			left = right
		return res

	def maxChunksToSorted3(self, arr):
		from collections import Counter
		res = 0
		n = len(arr)
		arr_copy = arr[:]
		arr_copy.sort()
		arr_copy_dict = Counter()
		arr_dict = Counter()
		for i in range(n):
			arr_copy_dict[arr_copy[i]] += 1
			arr_dict[arr[i]] += 1
			if arr_copy_dict == arr_dict:
				res += 1
				arr_copy_dict.clear()
				arr_dict.clear()
		return res




a = Solution()
print(a.maxChunksToSorted1([1,0,2,3,4]))
print(a.maxChunksToSorted1([4,3,2,1,0]))
print(a.maxChunksToSorted1([1,4,3,6,0,7,8,2,5]))


