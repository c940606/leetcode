class Solution(object):
	def convertToTitle(self, n):
		"""
		给定一个正整数，返回它在 Excel 表中相对应的列名称。
		---
		 		 1 -> A
				2 -> B
				3 -> C
				...
				26 -> Z
				27 -> AA
				28 -> AB
				...
		---
		输入: 1
		输出: "A"
		--
		输入: 28
		输出: "AB"
		---
		输入: 701
		输出: "ZY"
		---

		:type n: int
		:rtype: str
		"""
		lookup = {
			1: 'A',
			 2: 'B',
			 3: 'C',
			 4: 'D',
			 5: 'E',
			 6: 'F',
			 7: 'G',
			 8: 'H',
			 9: 'I',
			 10: 'J',
			 11: 'K',
			 12: 'L',
			 13: 'M',
			 14: 'N',
			 15: 'O',
			 16: 'P',
			 17: 'Q',
			 18: 'R',
			 19: 'S',
			 20: 'T',
			 21: 'U',
			 22: 'V',
			 23: 'W',
			 24: 'X',
			 25: 'Y',
			 0: 'Z'
		}
		s = ""
		while True:

			trading,remainder = divmod(n,26)
			print("shang:",trading,"yu:",remainder)
			s = lookup[remainder]+s
			n = trading
		return s

	def convertToTitle1(self, n):
		result, dvd = "", n
		while dvd:
			result += chr((dvd - 1) % 26 + ord('A'))
			dvd = (dvd - 1) // 26
		return result[::-1]

a = Solution()
print(a.convertToTitle(52))
