from functools import lr
class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):
		"""
		假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
		可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
		给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），
		和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
		--
		输入: flowerbed = [1,0,0,0,1], n = 1
		输出: True
		--
		思路：
		先找到可以种植区域
		种上 更新 可行区域
		:type flowerbed: List[int]
		:type n: int
		:rtype: bool
		"""
		if n == 0:
			return True
		# length = len(flowerbed)
		can_area = []
		one_area = []
		for idx,num in enumerate(flowerbed):
			if num == 0:
				can_area.append(idx)
			else:
				one_area.append(idx)
		print("can_area:",can_area)
		print("one_area:",one_area)
		for i in one_area:
			if i-1 in can_area:
				can_area.remove(i-1)
			if i+1 in can_area:
				can_area.remove(i+1)
		def helper(i,can_area):
			if i-1 in can_area:
				can_area.remove(i-1)
			elif i+1 in can_area:
				can_area.remove(i+1)
		print(can_area)
		if len(can_area) < n:
			return False
		count = 0
		i = 0
		while can_area and count < n:
			count += 1

			helper(can_area[i],can_area)
			can_area.pop(i)
			print(can_area)
		return count == n

	def canPlaceFlowers1(self, flowerbed, n):
		count = 0
		length = len(flowerbed)
		if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
			print("第一个")
			count += 1
			flowerbed[length-1] = 1
		if flowerbed[0] == 0 and flowerbed[1] == 0:
			print("第二个")
			count += 1
			flowerbed[0] = 1
		print(flowerbed)
		for i in range(1,length -2):

			if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
				print("循环：",i)
				count += 1
				flowerbed[i] = 1
		print(count)
		if count >= n:
			return True
		else:
			return False

a = Solution()
print(a.canPlaceFlowers1(flowerbed = [1,0,0,0,1], n = 1))
# print(a.canPlaceFlowers1([1,0,0,0,0,1],2))
# print(a.canPlaceFlowers1([0,1,0],1))
# print(a.canPlaceFlowers1([1,0,0,0,1,0,0],2))