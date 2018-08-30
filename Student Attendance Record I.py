class Solution(object):
	def checkRecord(self, s):
		"""
		给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：
		'A' : Absent，缺勤
		'L' : Late，迟到
		'P' : Present，到场
		如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
		你需要根据这个学生的出勤纪录判断他是否会被奖赏。
		---
		输入: "PPALLP"
		输出: True
		---
		思路：
		记录 L A 的个数
		A 直接记录
		L 要判断连续
		:type s: str
		:rtype: bool
		"""
		n = len(s)
		i = 0
		A_num = 0
		L_num = 0
		while (A_num < 2 and L_num < 3) and i < n:
			L_num = 0
			if s[i] == "P":
				i += 1
				continue
			if s[i] == "A":
				A_num += 1
				i += 1
				continue
			while i < n and s[i] == "L" and L_num < 3:
				i += 1
				L_num += 1
			# i += 1
			print(i,A_num,L_num)
		if  A_num < 2 and L_num <3:
			return True
		else:
			return False
a = Solution()
print(a.checkRecord("PPALLP"))

