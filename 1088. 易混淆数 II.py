class Solution:
    def confusingNumberII(self, N: int) -> int:

        visited = set()
        def helper1(tmp):
            lookup = {
                "1": "1",
                "0": "0",
                "6": "9",
                "8": "8",
                "9": "6"
            }
            #N_str = str(N)
            t = ""
            for alp in tmp:
                if alp in lookup:
                    t += lookup[alp]
                else:
                    return False
            return tmp != t[::-1]
        #print(helper1("99"))

        def helper(tmp, num):
            #print(tmp)
            if tmp and tmp[0] != "0" and int(tmp) <= N and helper1(tmp):
                visited.add(tmp)
            if tmp and int(tmp) > N:
                return

            for i in range(len(num)):
                if not tmp :
                    if num[i] != "0":
                        helper(tmp + num[i], num)
                else:
                    if int(tmp) > N:
                        break
                    helper(tmp + num[i], num)
        helper("", ["0", "1","6","8","9"])
        #print(sorted(visited))
        return len(visited)
        # res = 0
        # for i in range(1, N+1):
        #     if helper1(str(i)):
        #         res += 1
        # return res

a = Solution()
# print(a.confusingNumberII(20))
# print(a.confusingNumberII(100))
# print(a.confusingNumberII(10**9))
# print(a.confusingNumberII(2999847))
# print(a.confusingNumberII(3999877))
# print(a.confusingNumberII(3999915))
# print(a.confusingNumberII(2999936))
# print(a.confusingNumberII(3999819))
# print(a.confusingNumberII(100000000))
# print(a.confusingNumberII(3999870))
print(a.confusingNumberII(1000000000))