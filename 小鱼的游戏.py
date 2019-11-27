h1, m1, h2, m2 = map(int, input().split())
# timeh = h2 - (h1 + 1)
# timem = m2 + (60 - m1)
# if timem >= 60:
#     timem -= 60
#     timeh += 1
timeh = h1 * 60 + m1
timem = h2 * 60 + m2
sub = timem - timeh
print(sub // 60, sub % 60)
# print(timeh // 60, timem % 60)