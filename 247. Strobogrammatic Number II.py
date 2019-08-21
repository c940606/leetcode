class Solution:
    def findStrobogrammatic(self, n: int):
        res = []
        lookup = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        def helper1(tmp):
            ans = ""
            for t in tmp:
                ans += lookup[t]
            return ans[::-1]

        def helper(n, tmp):
            # print(n)
            if n == 0:
                res.append(tmp + helper1(tmp))
                return
            if n == 1:
                for num in ["0", "1",  "8", ]:
                    res.append(tmp + num + helper1(tmp))
                return

            for num in ["0", "1", "6", "8", "9"]:
                if not tmp and num == "0":
                    continue
                helper(n - 2, tmp + num)

        helper(n, "")
        return res


a = Solution()
print(a.findStrobogrammatic(3))
