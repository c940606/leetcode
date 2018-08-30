class Solution(object):
	def numRescueBoats(self, people, limit):
		"""
		第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
		每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
		返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
		---
		输入：people = [1,2], limit = 3
		输出：1
		解释：1 艘船载 (1, 2)
		---
		思路：
		只能做两个人 ，最大加最小的

		:type people: List[int]
		:type limit: int
		:rtype: int
		"""
		people.sort()
		n = len(people)
		i = 0
		j = n-1
		count = 0
		# print(people)
		while j>=i:

			# print(i,j)
			if people[i]+people[j] <= limit:
				count += 1
				i += 1
				j -= 1
			else:
				count += 1
				j -= 1
		return count
a = Solution()
print(a.numRescueBoats([3,5,3,4],5))
