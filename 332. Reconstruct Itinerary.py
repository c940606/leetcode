from typing import List


class Solution:
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        airports = defaultdict(int)
        res = []
        for x, y in tickets:
            graph[x].append(y)
            # 记录x到y次数
            airports[x + y] += 1
        print(graph)

        def dfs(i, tmp, airports):
            nonlocal res

            if len(tmp) == len(tickets) + 1:
                res = tmp
                return
            for j in sorted(graph[i]):
                if airports[i + j] > 0 and not res:
                    airports[i + j] -= 1
                    dfs(j, tmp + [j], airports)
                    airports[i + j] += 1

        dfs("JFK", ["JFK"], airports)

        return res

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        res = []
        for x, y in sorted(tickets)[::-1]:
            graph[x].append(y)

        def dfs(tmp):
            while graph[tmp]:
                dfs(graph[tmp].pop())
            res.append(tmp)

        dfs("JFK")
        return res[::-1]


a = Solution()
print(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(a.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
# print(a.findItinerary(
#     [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"],
#      ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]))
# print(a.findItinerary(
#     [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"],
#      ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"], ["AUA", "JFK"], ["JFK", "EZE"],
#      ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"],
#      ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"], ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"],
#      ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"],
#      ["ADL", "ANU"], ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"],
#      ["ADL", "EZE"], ["AXA", "TIA"], ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"], ["TIA", "AUA"],
#      ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"], ["TIA", "AXA"],
#      ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"], ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"],
#      ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"], ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"],
#      ["ANU", "AXA"], ["TIA", "ADL"], ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"],
#      ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
#      ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"], ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"],
#      ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"], ["AXA", "ADL"], ["EZE", "AUA"],
#      ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]]))
