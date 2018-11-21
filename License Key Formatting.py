class Solution(object):
	def licenseKeyFormatting(self, S, K):
		"""
		给定一个密钥字符串S，只包含字母，数字以及 '-'（破折号）。N 个 '-' 将字符串分成了 N+1 组。
		给定一个数字 K，重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符，
		第一个分组至少要包含 1 个字符。两个分组之间用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。
		给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。
		---
		输入：S = "5F3Z-2e-9-w", K = 4
		输出："5F3Z-2E9W"
		解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     	注意，两个额外的破折号需要删掉。
     	---
     	输入：S = "2-5g-3-J", K = 2
		输出："2-5G-3J"
		解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
		:type S: str
		:type K: int
		:rtype: str
		"""
		S = S.split("-")
		S = list(map(lambda x:x.upper(),S))
		s = "".join(S)
		s = s[::-1]
		n = len(s)
		res = []
		for i in range(0,n,K):
			res.append(s[i:i+K])
		print(res)
		return "-".join(res)[::-1]
a = Solution()
print(a.licenseKeyFormatting(S = "5F3Z-2e-9-w", K = 4))
print(a.licenseKeyFormatting(S = "2-5g-3-J", K = 2))
print(a.licenseKeyFormatting("2-4A0r7-4k",4))
