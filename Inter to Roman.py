class Solution:
	def intToRoman1(self, num):
		"""
		字符          数值
		I             1
		V             5
		X             10
		L             50
		C             100
		D             500
		M             1000
		-------------------------
		例子:
			输入: 3
			输出: "III"
		--------------------
			输入: 58
			输出: "LVIII"
			解释: C = 100, L = 50, XXX = 30, III = 3.
		---------------------------
			输入: 1994
			输出: "MCMXCIV"
			解释: M = 1000, CM = 900, XC = 90, IV = 4.

		:type num: int
		:rtype: str
		"""
		rom_dict = {
			4:{
				1000:"M",

			},
			3:{
				100:"C",
				400:"CD",
				500:"D",
				900:"CM"
			},
			2:{
				10:"X",
				40:"XL",
				50:"L",
				90:"XC"
			},
			1:{
				1:"I",
				4:"IV",
				5:"V",
				9:"IX"
			}
		}
		s = ""
		num_list = []
		count = 1
		while int(num):
			temp = (num%10)*count
			num_list.insert(0,temp)
			count *= 10
			num //= 10
		for i in num_list:
			n = len(str(i))
			base = 10**(n-1)
			temp = 5*base
			if i in rom_dict[n]:
				s += rom_dict[n][i]
			elif i > temp :
				s += rom_dict[n][temp]+rom_dict[n][base]*((i-temp)//base)
			else:
				s += rom_dict[n][base]*(i//base)
		return s

	def intToRoman2(self, num):
		look_up = {
			1000: "M",
			100: "C",
			400: "CD",
			500: "D",
			900: "CM",
			10: "X",
			40: "XL",
			50: "L",
			90: "XC",
			1: "I",
			4: "IV",
			5: "V",
			9: "IX"

		}
		s = ""
		for key,value in sorted(look_up.items(),key=lambda d:d[0],reverse=True):
			while num >= key:
				s += value
				num -= key
		return  s




a = Solution()
num1 = 3
num2 = 58
num3 = 1994
print(a.intToRoman1(num1))
print(a.intToRoman1(num2))
print(a.intToRoman1(num3))
print("------------------------------")
print(a.intToRoman2(num1))
print(a.intToRoman2(num2))
print(a.intToRoman2(num3))