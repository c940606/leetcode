import math

k = 1
res = 1


def dfs(n):
    global k, res
    if n == 1:
        return 1
    # tmp = (n - 1)* dfs(n - 1)
    # print(tmp)
    # # print(tmp)
    # # res = res + tmp + 1
    #print(dfs(n - 1) + math.factorial(3 - n) + 1)
    tmp = dfs(n - 1) + math.factorial(10 - n) + 1
    res += tmp
    return tmp
print(dfs(10))
print(res)
# num = math.factorial(9)
# print(num)
# n = 10
# cur = 1
# res = 1
# while n != 1 :
#     cur = num + 1 + cur
#     res += cur
#     num //= n
#     n -= 1
# print(res)
# def dfs(n, tmp):
#     if n == 0:
#         if tmp == 2050:
#             return True
#         else:
#             return False
#     if tmp > 2050:return False
#     print(tmp)
#     dfs(n - 1, tmp + 1)
#     dfs(n - 1, 2 * tmp)
#     return False
#
#
# print(dfs(24, 0))

# print(dfs(7))
# print(dfs(2))
# print(res)
