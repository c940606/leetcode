res = [0]

coins = [100, 50, 20, 10, 5, 1]
nums = [1, 2, 3, 4, 5, 6]


def process(i, chargers, tmp):
    #print(i, chargers, tmp)

    for j in range(i, 6):
        if coins[j] > chargers:
            continue
        if nums[j] > 0:
            nums[j] -= 1
            tmp += 1
            if chargers - coins[j] == 0:
                res[0] += tmp
                process(j + 1, chargers, tmp)


        else:
            process(j + 1, chargers, tmp)


process(0, 11, 0)
print(res[0])
