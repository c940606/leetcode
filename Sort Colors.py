from collections import Counter


class Solution:
	def sortColors(self, nums):
		"""
		给定一个包含红色、白色和蓝色，一共 n 个元素的数组，
		原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
		此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
		输入: [2,0,2,1,1,0]
		输出: [0,0,1,1,2,2]
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		a = Counter(nums)
		nums.clear()
		nums.extend([[0]*a[0]+[1]*a[1]+[2]*a[2]])
		# return nums




a = Solution()
num = [2,0,2,1,1,0]
print (a.sortColors(num))