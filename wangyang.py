import functools


def customize_sort(x, y):
    cmp1_x = x[1]
    cmp2_y = y[1]

    for c1, c2 in zip(cmp1_x.split("."), cmp2_y.split(".")):
        if int(c1) > int(c2):
            return 1

    return -1


print(sorted([("123", "1.10"), ("123", "1.1"), ("123", "1.1")], key=functools.cmp_to_key(customize_sort)))
print(sorted([("123", "1.10"), ("124", "1.1"), ("123", "1.1")], key=lambda x: (x[1].split("."), x[0])))
