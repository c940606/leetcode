from collections import Counter
class Solution(object):
	def isLongPressedName(self, name, typed):
		"""
		:type name: str
		:type typed: str
		:rtype: bool
		"""
		n1 = len(name)
		n2 = len(typed)
		if n1 > n2:
			return False
		i = 0
		j = 0
		while i < n1 and j < n2:
			print(i,j)
			if name[i] == typed[j]:
				i += 1
				j += 1
			elif j > 0 and typed[j] == typed[j-1]:
				j += 1
			else:
				return False
		if i == n1 :
			return True
		return False

a = Solution()
# print(a.isLongPressedName("saeed","ssaaedd"))
print(a.isLongPressedName("pyplrz","ppyypllr"))