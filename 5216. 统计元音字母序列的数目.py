class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # 0 1 2 3 4
        # a e i o u
        pre = [1] * 5
        M = 10 ** 9 + 7
        for _ in range(n - 1):
            cur = [0] * 5
            cur[1] += pre[0]

            cur[0] += pre[1]
            cur[2] += pre[1]

            cur[0] += pre[2]
            cur[1] += pre[2]
            cur[3] += pre[2]
            cur[4] += pre[2]

            cur[2] += pre[3]
            cur[4] += pre[3]

            cur[0] += pre[4]
            pre = cur


        return sum(pre) % M


a = Solution()
print(a.countVowelPermutation(n=1))
print(a.countVowelPermutation(n=2))
print(a.countVowelPermutation(5))
print(a.countVowelPermutation(144))
