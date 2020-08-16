class Solution:
	def reverseStr(self, s: str, k: int) -> str:
		import re
		splitStr = re.findall(r".{%s}" % k, s)
		print(splitStr)


a = Solution()
print(a.reverseStr(s="abcdefg", k=2))
