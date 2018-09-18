# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	pass
class Solution(object):
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n<=1:
			return n
		if isBadVersion(1):
			return 1
		# version = list(range(1,n+1))
		i = 1
		j = n
		flag = 0
		while True:
			# print(i,j)

			mid = (i+j)//2
			if isBadVersion(mid):
				j = mid
			else:
				i = mid
			if flag == mid:
				return flag+1
			flag = mid