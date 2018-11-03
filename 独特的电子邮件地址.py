class Solution(object):
	def numUniqueEmails(self, emails):
		"""
		:type emails: List[str]
		:rtype: int
		"""
		if  not emails:
			return 0
		res = set()
		for email in emails:
			i = 0
			n = len(email)
			temp = ""
			while True:

				if email[i] == ".":
					i += 1
				temp += email[i]
				i += 1
				if email[i] == "+":
					while email[i] != "@":
						i += 1
					temp += email[i:]
					break
			res.add(temp)
		return len(res)
a = Solution()
print(a.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))