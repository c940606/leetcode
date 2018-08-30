class Solution(object):
	def peakIndexInMountainArray(self, A):
		"""
		我们把符合下列属性的数组 A 称作山脉：
		A.length >= 3
		存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
		给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
		---
		输入：[0,1,0]
		输出：1
		---
		输入：[0,2,1,0]
		输出：1
		--
		思路：
		二分法
		:type A: List[int]
		:rtype: int
		"""
		low,high = 0, len(A)-1
		while low <= high:
			mid = (low+high)//2
			if A[mid-1]<A[mid]>A[mid+1]:
				return mid
			elif A[mid-1]<A[mid]<A[mid+1]:
				low = mid+1
			elif A[mid-1]>A[mid]>A[mid+1]:
				high = mid-1
		return -1
a = Solution()
print(a.peakIndexInMountainArray([0,2,1,0]))
