class Solution:
    def addOperators1(self, num: str, target: int):

        res = []

        def dfs(num, tmp, cur, prev):
            # print(num, tmp, cur, prev)
            if not num:
                if cur == target:
                    res.append(tmp)
                return
            if max(1, abs(prev)) * (int(num)) < abs(target - prev):
                return
            for i in range(1, len(num) + 1):
                # print(i)
                val = num[:i]
                if len(val) > 1 and val[0] == "0": break
                ## +
                # print("df")
                if not prev:
                    dfs(num[i:], tmp + val, cur + int(val), int(val))
                else:
                    dfs(num[i:], tmp + "+" + val, cur + int(val), int(val))
                    # -
                    dfs(num[i:], tmp + "-" + val, cur - int(val), -int(val))
                    # *
                    dfs(num[i:], tmp + "*" + val, cur - prev + int(val) * prev, prev * int(val))

        dfs(num, "", 0, 0)
        return res

    def addOperators(self, num: str, target: int):
        res = []

        def helper(index, preOutStr, preSum, preValue):
            if index == len(num):
                if preSum == target:
                    res.append(preOutStr)
                return
            if max(1, abs(preValue)) * (int(num[index:])) < abs(target - preSum):
                return
            for i in range(index, index + 1 if num[index] == '0' else len(num)):
                cur = num[index:i + 1]
                curValue = int(cur)
                if not preOutStr:
                    helper(i + 1, cur, curValue, curValue)
                else:
                    helper(i + 1, preOutStr + '+' + cur, preSum + curValue, curValue)
                    helper(i + 1, preOutStr + '-' + cur, preSum - curValue, -curValue)
                    helper(i + 1, preOutStr + '*' + cur, preSum - preValue + curValue * preValue, curValue * preValue)

        helper(0, '', 0, 0)
        return res


a = Solution()
print(a.addOperators("123", 6))
# print(a.addOperators(num="232", target=8))
# print(a.addOperators(num="105", target=5))
# print(a.addOperators(num="00", target=0))
# print(a.addOperators(num="3456237490", target=9191))
