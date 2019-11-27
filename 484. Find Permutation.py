from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:

        # nums = list(range(len(s) + 1, 0, -1))
        # res = []
        # for i in range(len(s)):
        #     if s[i] == "D":
        #         if not res:
        #             tmp1 = nums.pop()
        #             tmp2 = nums.pop()
        #             res.extend([tmp2, tmp1])
        #         else:
        #             res.append(nums.pop())
        #             #print(i, res)
        #             for j in range(i, -1, -1):
        #                 if s[j] == "D" and res[j] < res[j + 1]:
        #                     res[j], res[j + 1] = res[j + 1], res[j]
        #                 elif s[j] == "I" and res[j] > res[j + 1]:
        #                     res[j], res[j + 1] = res[j + 1], res[j]
        #                 else:
        #                     break
        #     else:
        #         if not res:
        #             tmp1 = nums.pop()
        #             tmp2 = nums.pop()
        #             res.extend([tmp1, tmp2])
        #         else:
        #             res.append(nums.pop())
        #             #print(i, res)
        #             for j in range(i, -1, -1):
        #                 if s[j] == "D" and res[j] < res[j + 1]:
        #                     res[j], res[j + 1] = res[j + 1], res[j]
        #                 elif s[j] == "I" and res[j] > res[j + 1]:
        #                     res[j], res[j + 1] = res[j + 1], res[j]
        #                 else:
        #                     break
        # return res

        # from itertools import groupby
        # num = 1
        # res = []
        # for a, b in groupby(s):
        #     # print(res)
        #     n = len(list(b))
        #     if not res:
        #         if a == "D":
        #             res.extend(range(num + n, num - 1, -1))
        #         else:
        #             res.extend(range(num, num + n + 1, 1))
        #         num += (n + 1)
        #
        #     else:
        #         if a == "I":
        #             res.extend(range(num, num + n, 1))
        #         else:
        #             res.extend(list(range(num + n - 1, num - 1, -1)) + [res.pop()])
        #         num += n
        # return res
        from itertools import groupby
        lens = len(s) + 1
        num = list(range(1, lens + 1))
        res = [0] * lens
        # print(num, res)
        loc = 0
        for a, b in groupby(s):
            # print(res)
            n = len(list(b))
            if res[0] == 0:
                if a == "D":
                    # res.extend(range(num + n, num - 1, -1))
                    res[loc:loc + n + 1] = num[loc:loc + n + 1][::-1]

                else:
                    # res.extend(range(num, num + n + 1, 1))
                    res[loc:loc + n + 1] = num[loc:loc + n + 1]
                loc += (n + 1)

            else:
                if a == "I":
                    # res.extend(range(num, num + n, 1))
                    res[loc: loc + n] = num[loc:loc + n]
                else:
                    # res.extend(list(range(num + n - 1, num - 1, -1)) + [res.pop()])
                    res[loc - 1:loc + n] = num[loc:loc + n][::-1] + [res[loc - 1]]
                loc += n
        return res


a = Solution()
# print(a.findPermutation("I"))
print(a.findPermutation("DI"))
# print(a.findPermutation("DDDD"))
# print(a.findPermutation("IIII"))
# print(a.findPermutation("DIDIDIDD"))
# print(a.findPermutation("D" * 10000))
