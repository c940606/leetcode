from functools import cmp_to_key


class Solution(object):
    def largestNumber1(self, nums):
        """
        给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
        ---
        输入: [10,2]
        输出: 210
        ---
        输入: [3,30,34,5,9]
        输出: 9534330
        ---
        思路:

        :type nums: List[int]
        :rtype: str
        """

        def jup(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            elif x + y == y + x:
                return 0
            return 0

        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(lambda x, y: jup(x, y)))
        return "".join(nums)

    def largestNumber2(self, nums):
        from functools import cmp_to_key
        nums = [str(num) for num in nums]

        def helper(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        return "".join(sorted(nums, key=cmp_to_key(helper))).lstrip("0") or "0"

    def largestNumber5(self, nums):
        class cmp_large:
            def __init__(self, num):
                self.num = str(num)

            def __lt__(self, other):
                return self.num + other.num > other.num + self.num

            def __gt__(self, other):
                return self.num + other.num < other.num + self.num

            def __eq__(self, other):
                return self.num + other.num == other.num + self.num

        nums = [cmp_large(num) for num in nums]
        return "".join(a.num for a in sorted(nums)).lstrip("0") or "0"

    def largestNumber(self, nums):
        class large_num(str):
            def __lt__(self, other):
                return self + other > other + self

        return "".join(sorted(map(str, nums), key=large_num)).lstrip("0") or "0"


a = Solution()
# print(a.largestNumber([3, 30, 35]))
# print(a.largestNumber([3, 30, 34, 5, 9]))
print(a.largestNumber([0, 0]))
print(a.largestNumber([824, 8247]))
print(a.largestNumber([121, 12]))
