def romantoInt1(s):
	'''

	:param s:
	:return: int
	'''
	num_dict = {
		"I":1,
		"V":5,
		"X":10,
		# "IV":4,
		"IX":9,
		"L":50,
		"C":100,
		# "XL":40,
		# "XC":90,
		"D":500,
		"M":1000,
		# "CD":400,
		# "CM":900
	}
	n = len(s)
	left = 0
	split_list = []
	num = 0
	while left < n:
		if left+1 < n:
			if s[left]=="C" and (s[left+1]=="M" or s[left+1] == "D"):
				split_list.append(s[left:left+2])
				left += 2
			elif s[left] == "X" and (s[left+1]=="L" or s[left+1]=="C"):
				split_list.append(s[left:left + 2])
				left += 2
			elif s[left] == "I" and (s[left+1]=="V" or s[left+1]=="X"):
				split_list.append(s[left:left + 2])
				left += 2
			else:
				split_list.append(s[left])
				left += 1
		else:
			split_list.append(s[left])
			left += 1
	for item in split_list:
		if len(item) == 2:
			num += num_dict[item[1]] - num_dict[item[0]]
		else:
			num += num_dict[item]
	return num

def romantoInt2(s):
	'''

	:param s:
	:return: int
	'''
	num_dict = {
		"I":1,
		"V":5,
		"X":10,
		# "IV":4,
		"IX":9,
		"L":50,
		"C":100,
		# "XL":40,
		# "XC":90,
		"D":500,
		"M":1000,
		# "CD":400,
		# "CM":900
	}
	num = 0
	n = len(s)
	for i in range(n):
		if i > 0 and num_dict[s[i-1]]<num_dict[s[i]]:
			num += num_dict[s[i]]-2*num_dict[s[i-1]]
		else:
			num += num_dict[s[i]]
	return  num



s1 = "III"
s2 = "IV"
s3 = "IX"
s4 = "LVIII"
s5 = "MCMXCIV"
print(romantoInt1(s1))
print(romantoInt1(s2))
print(romantoInt1(s3))
print(romantoInt1(s4))
print(romantoInt1(s5))
print("-------------------------------------")
print(romantoInt2(s1))
print(romantoInt2(s2))
print(romantoInt2(s3))
print(romantoInt2(s4))
print(romantoInt2(s5))