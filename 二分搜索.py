def lower_bound(array, first, last, value):
	while first < last:
		mid = first + (last - first) // 2
		if array[mid] < value:
			first = mid + 1
		else:
			last = mid
	return first


def upper_bound(array, first, last, value):
	while first < last:
		mid = first + (last - first) // 2
		if array[mid] <= value:
			first = mid + 1
		else:
			last = mid
	return first


a = [1, 2, 2, 3, 3, 4, 4]
print(lower_bound(a, 0, 7, 3))
print(upper_bound(a, 0, 7, 3))
