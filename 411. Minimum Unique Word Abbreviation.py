class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        import re
        # 把长度一样找出来， 因为长度不一样缩写一定不一样
        filter_dictionary = []
        # target 所有缩写词
        res = []
        n = len(target)
        for dis in dictionary:
            if len(dis) == n:
                filter_dictionary.append(dis)
        if not filter_dictionary: return str(n)

        # 每个缩写词的长度
        def cmp(t):
            return len(re.findall(r"[0-9]+|[a-z]", t))

        # 回溯算法找出所有缩写
        def helper(i, tmp):
            if i == n:
                res.append(tmp)
            else:
                for j in range(i, n):
                    num = str(j - i) if j - i > 0 else ""
                    helper(j + 1, tmp + num + target[j])
                helper(n, tmp + str(n - i))

        helper(0, "")

        # 判断abbr是否是word的缩写词
        def vaild(abbr, word):
            i = 0
            j = 0
            m = len(word)
            n = len(abbr)
            while i < m and j < n:
                if abbr[j].isdigit():
                    if abbr[j] == "0": return False
                    num = 0
                    while j < n and abbr[j].isdigit():
                        num = num * 10 + int(abbr[j])
                        j += 1
                    i += num
                else:
                    if word[i] != abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == m and j == n

        # 排序
        res.sort(key=cmp)
        for abbr in res:
            if not any(vaild(abbr, word) for word in filter_dictionary):
                return abbr


a = Solution()
print(a.minAbbreviation("apple", ["blade"]))
print(a.minAbbreviation("apple", ["plain", "amber", "blade"]))
print(a.minAbbreviation("usaandchinaarefriend", ["fda"]))
