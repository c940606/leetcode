class Solution:
    def groupStrings(self, strings):
        strings = sorted(strings, key=len)
        i = 0
        n = len(strings)
        res = []

        def check(s, t):
            a = set()
            for i, j in zip(s, t):
                a.add((ord(i) - ord(j)) % 26)
            return len(a) == 1

        def helper(tmp):
            visited = set()
            for i in range(len(tmp)):
                if i not in visited:
                    tmp_list = [tmp[i]]
                    visited.add(i)
                    for j in range(len(tmp)):
                        if j not in visited:

                            if check(tmp[i], tmp[j]):
                                visited.add(j)
                                tmp_list.append(tmp[j])
                    res.append(tmp_list)

        while i < n:
            left = i
            while i < n - 1 and len(strings[i]) == len(strings[i + 1]):
                i += 1
            helper(strings[left: i + 1])
            i += 1
        return res


a = Solution()
# print(a.groupStrings(["abc", "bcd", "acef", "xyz", "az", "cb", "a", "z"]))
print(a.groupStrings(["ab","ba"]))
