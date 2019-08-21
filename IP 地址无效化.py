class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for a in address:
            if a == ".":
                res += "[.]"
            else:
                res += a
        return res


a = Solution()
print(a.defangIPaddr("1.1.1.1"))
print(a.defangIPaddr("255.100.50.0"))
