def atoi(s):
	'''
	:param s:
	:return: 返回字符串里的数字
	'''
	num_list = [str(i) for i in range(10)]
	s = s.strip()
	n = len(s)
	num_str = ""
	flag = 0
	if (s[0] in num_list) or (s[0] == "+") or (s[0] == "-"):
		num_str += s[0]
	else:
		return 0
	for item in s[1:]:
		if item in num_list :

			flag += 1
			num_str += item
		elif item not in num_list and flag > 0:
			break
	if num_str == "+" or num_str == "-":
		return 0
	num = int(num_str)
	if num>2**31-1:
		return " INT_MAX (2**31 − 1) "
	elif num < -2**31:
		return "INT_MIN (−2**31)"
	else:
		return num
s1 = "    -42"
s2 = "4193 with words"
s3 = "words and 987"
s4 = "-91283472332"
s5 = "32423 ksdjf234234"
print(atoi(s1))
print(atoi(s2))
print(atoi(s3))
print(atoi(s4))
print(atoi(s5))






