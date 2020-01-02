# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber1(self, n: int) -> int:

        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid
        return left

    def guessNumber(self, n: int) -> int:
        import bisect
        class C:
            def __getitem__(self, item):
                return -guess(item)
        return bisect.bisect_left(C(), 0, 1, n)