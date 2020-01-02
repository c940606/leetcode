class Solution(object):
    def lastRemaining4(self, n):
        """
        给定一个从1 到 n 排序的整数列表。
        首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
        第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
        我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
        返回长度为 n 的列表中，最后剩下的数字。
        ---
        输入:
        n = 9,
        1 2 3 4 5 6 7 8 9
        2 4 6 8
        2 6
        6
        输出:
        6
        ---
        :type n: int
        :rtype: int
        """
        res = list(range(1, n + 1))
        while True:
            res = res[1::2]
            print(res)
            if len(res) == 1:
                break
            res = res[-2::-2][::-1]
            print(res)
            if len(res) == 1:
                break
        return res[0]

    def lastRemaining1(self, n):
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))

    def lastRemaining2(self, n):
        from collections import deque
        res = deque((range(1, n + 1)))
        # print(res)
        flag = 1
        while len(res) != 1:
            tmp = deque()
            if flag % 2 == 1:
                for i in range(1, len(res), 2):
                    tmp.append(res[i])
            else:
                for i in range(len(res) - 2, -1, -2):
                    tmp.appendleft(res[i])
            res = tmp
            flag += 1
        return res[0]

    def lastRemaining3(self, n):
        left = True
        head = 1
        remaining = n
        step = 1
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            left = not left
            step *= 2
        return head

    def lastRemaining6(self, n: int) -> int:

        arr = list(range(1, n + 1))
        flag = True

        while len(arr) > 1:
            # print(arr)
            next_arr = []
            if flag:
                for i in range(1, len(arr), 2):
                    next_arr.append(arr[i])
            else:
                for i in range(len(arr) - 2, -1, -2):
                    next_arr.insert(0, arr[i])
            flag = not flag
            arr = next_arr
        return arr[0]

    def lastRemaining(self, n: int) -> int:
        remain = n
        flag = True
        res = 1
        step = 1
        while remain > 1:
            if flag or remain % 2 == 1:
                res += step
            flag = not flag
            step *= 2
            remain //= 2
        return res


a = Solution()
# print(a.lastRemaining(9))
# print(a.lastRemaining6(1))
# print(a.lastRemaining6(6))
# print(a.lastRemaining(100000000))
# print(a.lastRemaining6(9))
# print(a.lastRemaining6(100))
for i in range(1, 100):
    print(i, a.lastRemaining(i))
