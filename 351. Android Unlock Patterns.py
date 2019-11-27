from itertools import permutations
import time

class Solution:
    def numberOfPatterns1(self, m: int, n: int) -> int:
        t1 = time.time()
        def helper(tmp):
            prev = tmp[0]
            visited = set([prev])
            for t in tmp[1:]:
                abs_t = abs(t - prev)
                if abs(t - prev) == 6 and (t + prev) // 2 not in visited:
                    return False
                if abs_t == 4 and min(prev, t) == 3 and 5 not in visited:
                    return False
                if abs_t == 8 and 5 not in visited:
                    return False
                if abs_t == 2 and min(prev, t) in {1, 4, 7} and (t + prev) // 2 not in visited:
                    return False

                visited.add(t)
                prev = t
            return True

        res = 0
        for i in range(m, n + 1):
            for tmp in permutations(range(1, 10), i):
                if helper(tmp):
                    res += 1
        t2 = time.time()
        print(t2 - t1)
        return res

    def numberOfPatterns(self, m: int, n: int) -> int:
        #t1 = time.time()
        self.res = 0
        all_set = set(range(1, 10))

        def backtrack(cur_set, prev):
            if len(cur_set) >= m:
                self.res += 1
                if len(cur_set) == n:
                    return
            for num in all_set - cur_set:
                abs_t = abs(num - prev)
                if abs_t == 2 and min(num, prev) in {1, 4, 7} and (num + prev) // 2 not in cur_set: continue
                if abs_t == 4 and min(num, prev) == 3 and 5 not in cur_set: continue
                if abs_t == 6 and (num + prev) // 2 not in cur_set: continue
                if abs_t == 8 and 5 not in cur_set: continue
                backtrack(cur_set | {num}, num)

        for i in range(1, 10):
            backtrack({i}, i)
        #t2 = time.time()
        #print(t2 - t1)
        return self.res


a = Solution()
print(a.numberOfPatterns(4, 9))
print(a.numberOfPatterns1(4, 9))
