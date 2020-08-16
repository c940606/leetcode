class Solution:
    def findComplement(self, num: int) -> int:
        # res = ""
        # for n in bin(num)[2:]:
        #     if n == "1":
        #         res += "0"
        #     else:
        #         res += "1"
        # return int(res, 2)

        # return int("".join(map(lambda x: "0" if x == "1" else "1", bin(num)[2:])), 2)
        bit_num = bin(num)[2:]
        mask = "1" * (len(bit_num))
        return bit_num ^ mask