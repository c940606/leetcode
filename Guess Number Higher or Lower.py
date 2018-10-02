class Solution(object):
	def guessNumber(self, n,k):
		left = 1
		right = n
		while left <= right:
			mid = (left+right)//2

			if mid == k:
				return 0
			elif mid > k:
				right = mid-1
			else:
				left = mid+1
a = Solution()
print(a.guessNumber(10,6))