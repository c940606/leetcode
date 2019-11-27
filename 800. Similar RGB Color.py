class Solution:
    def similarRGB(self, color: str) -> str:
        color = color[1:]
        res = ""
        min_num = float("-inf")
        for a in "0123456789abcdef":
            for b in "0123456789abcdef":
                for c in "0123456789abcdef":
                    tmp = -(int(color[:2], 16) - int(a * 2, 16)) ** 2 - (int(color[2:4], 16) - int(b * 2, 16)) ** 2 - (
                            int(color[4:6], 16) - int(c * 2, 16)) ** 2

                    if tmp > min_num:
                        res = a * 2 + b * 2 + c * 2
                        min_num = tmp
        return "#" + res

a = Solution()
print(a.similarRGB("#09f166"))
