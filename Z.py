# s = "qweryu7"
# n = len(s)
# i = 0
# while 3+6*i<n:
# 	i += 1
# print(1+3*i)

#建立矩阵
def loc(s,row):
	n = len(s)
	num = 0
	while row + 2*(row-1)*num<n:
		num += 1
	col = 1 + (row-1)*num
	maxic = [[None]*col for _ in range(row)]
	#填充位置
	i = 0
	j = 0
	for item in s:
		if j%(row-1) == 0:
			maxic[i][j] = item
			i += 1
			if i == row:
				j += 1
				i -= 2
		else:
			maxic[i][j] = item
			i -= 1
			j += 1
			if i == -1:
				i += 2
				j -= 1
	return maxic

def print_Z(maxic):
	Z_list =[]
	for i in range(len(maxic)):
		for j in range(len(maxic[0])):
			if maxic[i][j] != None:
				Z_list.append(maxic[i][j])
	return "".join(Z_list)






s = "PAYPALISHIRING"
maxic1 = loc(s,3)
print(print_Z(maxic1))