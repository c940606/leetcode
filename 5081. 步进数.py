class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        from collections import deque
        res = set()

        if low == 0:
            res.add(0)
        n = len(str(high))
        for i in range(1, 10):
            queue = deque()
            queue.appendleft(str(i))

            while queue:
                #print(queue)
                tmp = queue.pop()
                if low <= int(tmp) <= high:
                    res.add(int(tmp))
                t = int(tmp[-1])
                tmp1 = ""
                tmp2 = ""
                if t != 0:
                    tmp2 = tmp + str(t - 1)
                if t!= 9:
                    tmp1 = tmp + str(t + 1)
                #print(tmp1, tmp2)
                if tmp1 and int(tmp1) <= high:
                    queue.appendleft(tmp1)
                if  tmp2 and int(tmp2) <= high:
                    queue.appendleft(tmp2)
        return sorted(res)


a = Solution()
print(a.countSteppingNumbers(0,  10 ** 9))
# print(a.countSteppingNumbers(10, 15))
