class Solution:
    def twoCitySchedCost(self, costs) -> int:
        # if not costs:
        #     return 0
        n = len(costs) // 2
        visited = set()
        A_visited = set()
        B_visited = set()
        all_data = []
        for idx, cost in enumerate(costs):
            all_data.append((cost[0], idx, "A"))
            all_data.append((cost[1], idx, "B"))
        res = 0

        all_data.sort()
        print(all_data)
        for cost, idx, flag in all_data:
            if idx not in visited:
                if flag == "A":
                    if len(A_visited) == n:
                        continue
                    if idx not in A_visited:
                        res += cost
                        A_visited.add(idx)
                else:
                    if len(B_visited) == n:
                        continue
                    if idx not in B_visited:
                        res += cost
                        B_visited.add(idx)
                visited.add(idx)
        print(visited, A_visited, B_visited)
        return res

    def twoCitySchedCost1(self, costs) -> int:

        self.res = float("inf")
        self.n = len(costs)

        def helper(i, tmp, A_visited, B_visited):
            if len(A_visited) > self.n // 2 or len(B_visited) > self.n // 2:
                return
            if i == self.n and len(A_visited) == self.n // 2 and len(B_visited) == self.n // 2:
                self.res = min(self.res, tmp)
                return
            helper(i + 1, tmp + costs[i][0], A_visited | {i}, B_visited)
            helper(i + 1, tmp + costs[i][1], A_visited, B_visited | {i})

        helper(0, 0, set(), set())
        return self.res

    def twoCitySchedCost2(self, costs) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        res = 0
        for i in range(n):
            res += (costs[i][0] + costs[n + i][1])
        return res

    def twoCitySchedCost3(self, costs) -> int:
        data = []
        i = 0
        for x, y in costs:
            data.append((x - y, i))
            i += 1
        data.sort()
        #print(data)
        all_cost_A = 0
        for x, y in costs:
            all_cost_A += x
        for val, idx in data[len(costs) // 2:]:
            all_cost_A -= val
        return all_cost_A


a = Solution()
print(a.twoCitySchedCost3([[10, 20], [30, 200], [400, 50], [30, 20]]))
print(a.twoCitySchedCost2([]))
print(a.twoCitySchedCost2([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
print(a.twoCitySchedCost2(
    [[289, 393], [484, 287], [317, 704], [192, 126], [699, 429], [100, 85], [482, 352], [976, 727], [240, 569],
     [621, 492], [189, 936], [437, 616], [597, 458], [703, 858], [258, 923], [524, 558], [240, 502], [861, 228],
     [840, 463], [130, 742], [653, 402], [836, 430]]))
#
