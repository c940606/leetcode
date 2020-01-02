


def cal_min2(arr):
    num1 = float("inf")
    num2 = float("inf")
    for a in arr:
        if a < num1:
            num2 = num1
            num1 = a
        elif a < num2:
            num2 = a
    return num1, num2

print(cal_min2([1, 11, 9,10,3,5]))
    