num = input()
#num = "12"
res = set()


def helper(num, tmp):
    global res
    if not num:
        res.add(tmp)
        return
    if num[0] != "0":
        helper(num[1:], tmp + chr(int(num[0]) + 64))
    if num[0] != "0" and num[:2] <= "26":
        helper(num[2:], tmp + chr(int(num[:2]) + 64))


helper(num, "")
for item in sorted(res):
    print(item)
