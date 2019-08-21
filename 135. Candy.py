class Solution:
    def candy1(self, ratings) -> int:
        n = len(ratings)
        if n == 0: return 0
        left_to_right = [1] * n
        right_to_left = [1] * n
        # 找从左到右满足条件的
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # 保证从左到右的最少个数
                left_to_right[i] = left_to_right[i - 1] + 1
        # print(left_to_right)
        # 找从右到左满足条件的(同时要符合从左到右)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # 保证从左到右也满足, 同时也满足从右到左
                right_to_left[i] = max(left_to_right[i], right_to_left[i + 1] + 1)
        # print(right_to_left)
        res = 0
        # 选这个位置最大值
        for i in range(n):
            res += max(left_to_right[i], right_to_left[i])
        return res

    def candy2(self, ratings) -> int:
        n = len(ratings)
        if n == 0: return 0
        candy_nums = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_nums[i] = candy_nums[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy_nums[i - 1] = max(candy_nums[i - 1], candy_nums[i] + 1)
        return sum(candy_nums)

    def candy(self, ratings) -> int:
        res = 1
        pre = 1
        des_num = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if des_num > 0:
                    res += ((1 + des_num) * des_num) // 2
                    if pre <= des_num: res += (des_num - pre + 1)
                    pre = 1
                    des_num = 0
                if ratings[i] == ratings[i - 1]:
                    pre = 1
                else:
                    pre += 1
                res += pre
            else:
                des_num += 1
        # print(des_num)
        if des_num > 0:
            res += ((1 + des_num) * des_num) // 2
            if pre <= des_num: res += (des_num - pre + 1)
        return res
    


a = Solution()
print(a.candy([1, 0, 2]))
print(a.candy([1, 2, 2]))
