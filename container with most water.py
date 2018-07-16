def maxArea1(height):
	max_water = 0
	all_loc = []
	height = sorted(height)
	n = len(height)
	for index,Y_value in enumerate(height):
		X_value = index + 1
		loc = (X_value,Y_value)
		all_loc.append(loc)
	for i in range(n):
		for j in range(i+1,n):
			water_V = (all_loc[j][0]-all_loc[i][0])*min(all_loc[j][1],all_loc[i][1])
			if water_V > max_water:
				max_water = water_V
	return max_water
def maxArea2(height):
	max_wather = 0
	left = 0
	right = len(height)-1
	while left <= right:
		max_wather = max(max_wather,(right-left)*min(height[left],height[right]))
		if height[left]<height[right]:
			left += 1
		elif height[left]>height[right]:
			right -= 1
		else:
			left += 1
			right -= 1
	return max_wather


print(maxArea2([1,1,2,65,454,45]))

