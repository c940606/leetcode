class Solution(object):
	def findItinerary(self, tickets):
		"""
		给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，
		对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。
		说明:
		如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。
		例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
		所有的机场都用三个大写字母表示（机场代码）。
		假定所有机票至少存在一种合理的行程。
		---
		输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
		输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
		---
		输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
		输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
		解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
		---
		思路:
		先定义从某个地方出发 所有集合
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""

		# print(self.set_off("JFK",tickets))
		n = len(tickets)
		# print(n)
		res = []
		def dps(loc,tickets,n,temp):
			# print("dps:",loc,n,tickets)
			print(temp)
			# print("ticket:",tickets)
			print(n)
			if  n==0:
				print("n==0",temp)
				res.append(temp)
				return

			# print(loc,tickets)
			print(self.set_off(loc,tickets))
			for item in self.set_off(loc,tickets):
				print("循环:",item)
				if not item:
					return
				loc_index = tickets.index(item)
				if not self.set_off(item[1], tickets[:loc_index] + tickets[loc_index + 1:]) and n > 1:
					continue
				if not  self.set_off(item[1],tickets[:loc_index]+tickets[loc_index+1:]) and n == 1:
					dps(item[1], tickets[:loc_index] + tickets[loc_index + 1:], n - 1, temp + item)
					return


				if self.set_off(item[1],tickets[:loc_index]+tickets[loc_index+1:]):
					dps(item[1],tickets[:loc_index]+tickets[loc_index+1:],n-1,temp+[item[1]])
					return
			return



		dps("JFK", tickets, n, ["JFK"])
		# print("---")

		return res

	def set_off(self,loc, tickets):
		res = []
		for item in tickets:
			if item[0] == loc:
				res.append(item)
		res.sort()
		return res
a = Solution()


data = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
print(a.findItinerary(data))