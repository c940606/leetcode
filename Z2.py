def convert_Z(s,rowNum):
	if rowNum == 1 or rowNum >= len(s):
		return s
	Z_row = [""]*rowNum
	index = 0
	footStep = 1
	for item in s:
		if footStep == 1:
			if index < rowNum:
				Z_row[index] += item
				index += footStep
			if index == rowNum:
				footStep = -1
				index = rowNum-1
		else:
			if index > -1:
				index += footStep
				Z_row[index] += item
			if index == 0:
				footStep = 1
				index = 1
	return Z_row
def convert_Z1(s,rowNum):
	if rowNum == 1 or rowNum >= len(s):
		return s
	Z_row = [""]*rowNum
	index = 0
	footStep = 0
	for item in s:
		Z_row[index] += item
		if index == 0:
			footStep = 1
		elif index == rowNum-1:
			footStep = -1
		index += footStep
	return "".join(Z_row)



print(convert_Z1("abcdefghijklmn", 4))


