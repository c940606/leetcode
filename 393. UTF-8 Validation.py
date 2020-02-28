class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data: return False
        data = [bin(d)[2:].rjust(8, "0") for d in data]
        i = 0
        while i < len(data):
            num = data[i].find("0")
            if num == 1 or num == -1 or num >= 5: return False
            if num == 0:
                i += 1
                continue
            if i + 1 < len(data) and data[i + 1][0] == "0":
                i += 1
                continue
            for j in range(i + 1, i + num):
                if j >= len(data) or data[j][:2] != "10":
                    return False
            i += num
        return True
