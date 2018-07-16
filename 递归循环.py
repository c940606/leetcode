# def


def cycle(s,str):

	if len(str) == 0:
		# print("+++++++++++++++")
		return list2.append(s)

	for i in str[0]:
		# print("-------------")
		# s += i
		# print(t)
		cycle(s+i, str[1:])
		print("------------")
		# print(t)
		# s += t
		# # print("==========")
		# list2.append(s)

list2 = []
print(list2)
str1 = ["abc","dsfa"]
print(cycle("", str1))
print(list2)
# print(list2)