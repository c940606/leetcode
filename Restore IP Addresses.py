class Solution:
	def restoreIpAddresses(self, s):
		"""
		给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
		---
		输入: "25525511135"
		输出: ["255.255.11.135", "255.255.111.35"]
		:type s: str
		:rtype: List[str]
		"""
		self.res = []
		if len(s) > 15:
			return []
		self.dps("",s,3)
		return self.res

	def dps(self,temp,s,n):
		# print(temp)

		# if temp and int(temp.split(".")[-2])>255:
		# 	# print(temp.split(".")[-2])
		# 	return

		if not s:
			return
		if n == 0:
			# print(temp+s)
			split_s = (temp+s).split(".")
			for item in split_s:
				if len(item)>1 and item[0]=="0":
					return
			if max(map(int,split_s )) <= 255:
				self.res.append(temp+s)
			# return
		#
		# if temp[:-1] > "255":
		# 	return


		for i in range(0,len(s)):
			# print(temp+s[0:i+1])
			# if temp.split(".")[-1] > "255":
			# 	break

			self.dps(temp+s[0:i+1]+".",s[i+1:],n-1)
			# temp += "."
a = Solution()
#"010010"
print(a.restoreIpAddresses("010010"))
