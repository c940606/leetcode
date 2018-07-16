def F(x):
	if x == 1:
		print("===============")
		return 1
	elif x == 2:
		print("-------------")
		return 1
	else:
		print("递归前")
		a = F(x-1)
		b = F(x-2)
		s =  a + b
		print("递归后")
		return s
print(F(4))