#https://blog.csdn.net/chibangyuxun/article/details/53012537
# 归并排序
def MergeSort(lists):
	if len(lists) <= 1:
		return lists
	mid = len(lists)//2
	# 递归
	listA = MergeSort(lists[:mid])
	listB = MergeSort(lists[mid:])
	print("============listA========")
	print(listA)
	print("============listB==========")
	print(listB)
	return MergeSortedLists(listA,listB)
def MergeSortedLists(listA,listB):
	newList = []
	a = 0
	b = 0
	while a < len(listA) and b < len(listB):
		if listA[a] < listB[b]:
			newList.append(listA[a])
			a += 1
		else:
			newList.append(listB[b])
			b += 1
	while a < len(listA):
		newList.append(listA[a])
		a += 1
	while b < len(listB):
		newList.append(listB[b])
		b += 1
	return newList

if __name__ == '__main__':
	lists = [3,5,4,2,1,6]
	print(lists)
	result = MergeSort(lists)
	print(result)