import bisect
# 求下界
# x >= value or x > value

# 求上界

a = [0, 0, 1, 3, 3, 3, 5, 5]
b = []
# print(bisect.bisect_left(a, 0, 1))
# print(bisect.bisect_right(a, 0, lo = 1) - 1)

# 1.找等于val的左右边界
## 1.1 val = 0
val = 5
print(bisect.bisect_left(a, val)) # 左
print(bisect.bisect_left(a,  val + 1) - 1) # 右
print(bisect.bisect_right(a, val) - 1) # 右

# 找小于等于val最大值
val = 4
print(bisect.bisect_right(a, val) - 1)

# 找大于等于val最小值
print(bisect.bisect_left(a, 2))
