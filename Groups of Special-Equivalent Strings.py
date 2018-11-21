class Solution(object):
	def numSpecialEquivGroups(self, A):
		"""
		:type A: List[str]
		:rtype: int
		"""
		if not A:
			return 0
		t = set()
		for s in A:
			odd = [0]*26
			even = [0]*26
			for idx,alp in enumerate(s):
				if idx %2 == 1:
					odd[ord(alp)-97] += 1
				else:
					even[ord(alp) - 97] += 1
			temp = "".join(map(str,odd)) + "".join(map(str,even))
			t.add(temp)
		return len(t)
a = Solution()
print(a.numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))
