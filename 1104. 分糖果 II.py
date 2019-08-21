class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        res = [0] * num_people
        i = 1
        loc = 0
        while candies:
            if candies >= i:

                candies -= i
                res[loc] += i
            else:
                res[loc] += candies
                candies = 0

            i += 1
            loc = (loc + 1) % num_people
        return res




a = Solution()
print(a.distributeCandies(candies=7, num_people=4))
print(a.distributeCandies(candies=10, num_people=3))
