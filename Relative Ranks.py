class Solution(object):
	def findRelativeRanks(self, nums):
		"""
		给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
		前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
		(注：分数越高的选手，排名越靠前。)
		---
		输入: [5, 4, 3, 2, 1]
		输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
		解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
		余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
		:type nums: List[int]
		:rtype: List[str]
		"""
		sort_nums = sorted(nums,reverse=True)
		for idx,num in enumerate(sort_nums):
			if idx+1 == 1:
				nums[nums.index(num)] = "Gold Medal"
			elif idx + 1 == 2:
				nums[nums.index(num)] = "Silver Medal"
			elif idx + 1 == 3:
				nums[nums.index(num)] = "Bronze Medal"
			else:
				nums[nums.index(num)] = idx+1
		return nums
a = Solution()
print(a.findRelativeRanks([5, 4, 3, 2, 1]))