class Solution:
    def canMeasureWater1(self, x: int, y: int, z: int) -> bool:
        from collections import deque
        queue = deque([[0, 0]])
        visited = set([(0, 0)])

        while queue:
            cur_x, cur_y = queue.pop()
            if z in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [
                # 加满水
                (x, cur_y), (cur_x, y),
                # 清空水
                (0, cur_y), (cur_x, 0),
                # x -> y
                (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
                # y -> x
                (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
                if item not in visited:
                    queue.appendleft(item)
                    visited.add(item)
        return False

    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
        visited = set()

        def helper(cur_x, cur_y):
            print(cur_x, cur_y)
            if z in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [
                # 加满水
                (x, cur_y), (cur_x, y),
                # 清空水
                (0, cur_y), (cur_x, 0),
                # x -> y
                (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
                # y -> x
                (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
                if item not in visited:
                    visited.add(item)
                    if helper(*item): return True
                    visited.remove(item)

            return False

        return helper(x, y)

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        if x + y < z: return False
        if x == z or y == z or x + y == z: return True
        return z % math.gcd(x, y) == 0


a = Solution()
print(a.canMeasureWater(3, 5, 4))
print(a.canMeasureWater(2, 6, 5))
print(a.canMeasureWater(104579, 104593, 12444))
