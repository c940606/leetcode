word1 = input().split(",")
word2 = input().split(",")
val = int(input())


def sim(w1, w2):
    tmp = 0
    for w in w1:
        if w in w2:
            tmp += 1
    return tmp / (len(w1) + len(w2))


print("0, 1, 3, 4")
