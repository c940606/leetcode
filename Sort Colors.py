from collections import Counter


class Solution:
    def sortColors2(self, nums):
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
        nums.extend([[0] * a[0] + [1] * a[1] + [2] * a[2]])

    # return nums
    def sortColors1(self, nums):
        c = Counter(nums)
        id = 0
        for i in range(3):
            if i in c:
                for j in range(c[i]):
                    nums[id] = i
                    id += 1
        return nums

    def sortColors3(self, nums):
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        #print(nums)
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
        #for i in range(len(nums), -1, -1):
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
        #print(nums)

    def sortColors(self, nums):
        left_zero = 0
        right_two = len(nums) - 1
        i = 0
        while i <= right_two:
            if nums[i] == 0:
                nums[i], nums[left_zero] = nums[left_zero],nums[i]
                left_zero += 1
            elif nums[i] == 2:
                nums[i], nums[right_two] = num[right_two],nums[i]
                i -= 1
                right_two -= 1
            i += 1
        print(nums)


a = Solution()
num = [2, 0, 2, 1, 1, 0]
num1 = [1]
print(a.sortColors(num))
print(a.sortColors([0, 1, 2]))
print(a.sortColors([1, 0, 2]))
