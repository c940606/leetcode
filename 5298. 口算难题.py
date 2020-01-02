from typing import List


class Solution:
    def isSolvable2(self, words: List[str], result: str) -> bool:
        words.append(result)
        words_num = [0] * len(words)
        lookup = {}
        all_num = set(range(10))
        use_num = set()

        def search(pos, idx, cur):
            # print(pos, idx, cur)
            if pos == len(words):
                # print(words_num)
                _sum = 0
                for num in words_num[:-1]:
                    _sum += num
                _sum -= words_num[-1]
                return _sum == 0

            if idx == len(words[pos]):
                words_num[pos] = cur
                return search(pos + 1, 0, 0)
            alp = words[pos][idx]
            if alp in lookup:
                return search(pos, idx + 1, cur * 10 + lookup[alp])
            else:
                for tmp in all_num - use_num:
                    if idx == 0 and tmp == 0: continue
                    lookup[alp] = tmp
                    use_num.add(tmp)
                    if search(pos, idx + 1, cur * 10 + lookup[alp]):
                        return True
                    lookup.pop(alp)
                    use_num.remove(tmp)
            return False

        return search(0, 0, 0)

    def isSolvable1(self, words: List[str], result: str) -> bool:
        from itertools import permutations
        diff_alp = set()
        for word in words:
            diff_alp.update(word)
        diff_alp.update(result)
        diff_alp = list(diff_alp)

        def check(num):
            res = []
            for word in words:
                t = 0
                for w in word:
                    t = t * 10 + num[w]
                res.append(t)
            ans = 0
            for r in result:
                ans = ans * 10 + num[r]
            return sum(res) == ans

        for x in permutations(range(10), len(diff_alp)):
            num = {k: v for k, v in zip(diff_alp, x)}
            if check(num):
                return True
        return False

    def isSolvable4(self, words: List[str], result: str) -> bool:
        # 找最长字符串的长度
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))

        # 如果相加的字符串长度 大于 结果的长度
        if max_len > len(result): return False
        max_len = max(max_len, len(result))
        # 重塑words,把每个字符串拉长max_len,用"#" 补齐,
        constr_words = []
        for word in words:
            constr_words.append(word.rjust(max_len, "#"))
        # 结果同样也是
        result = result.rjust(max_len, "#")
        # 按位取出
        arr = []
        for x in zip(*constr_words, result):
            arr.append(x)
        # 取反(从低位开始
        arr = arr[::-1]
        # 每个arr元素长度
        l = len(arr[0])
        # 所有数字
        all_num = set(range(10))
        # 已经使用的数字
        used_num = set()
        # 记录每个字母代表数字
        lookup = {"#": 0}

        # pos 表示到arr索引, idx 表示 arr[pos]索引, carry进位
        def dfs(pos, idx, carry):
            # 递归出口
            if pos == len(arr):
                if carry == 0:
                    return True
                else:
                    return False
            # 求在pos位是否满足条件
            if idx == l:
                tmp = 0
                for t in arr[pos][:-1]:
                    tmp += lookup[t]
                tmp += carry
                a, b = divmod(tmp, 10)
                if b != lookup[arr[pos][-1]]: return False
                return dfs(pos + 1, 0, a)
            # 判断字符串是否在lookup
            if arr[pos][idx] in lookup:
                return dfs(pos, idx + 1, carry)
            else:
                # 枚举
                for num in all_num - used_num:
                    # 保证首位不能为0
                    if ((pos + 1 < len(arr) and arr[pos + 1][idx] == "#") or pos - 1 == len(arr)) and num == 0: continue
                    used_num.add(num)
                    lookup[arr[pos][idx]] = num
                    if dfs(pos, idx + 1, carry): return True
                    lookup.pop(arr[pos][idx])
                    used_num.remove(num)
            return False

        return dfs(0, 0, 0)

    def isSolvable(self, words: List[str], result: str) -> bool:
        max_len = 0
        all_num = set(range(10))
        use_num = set()
        for word in words:
            max_len = max(max_len, len(word))
        max_len = max(max_len, len(result))
        if max_len > len(result): return False
        lookup = {"#": 0}
        constr_words = []
        for word in words:
            constr_words.append(word.rjust(max_len, "#"))
        result = result.rjust(max_len, "#")
        arr = []
        for x in zip(*constr_words, result):
            arr.append(x)
        arr = arr[::-1]

        def dfs(pos, idx, carry):
            if pos == len(arr):
                if carry == 0:
                    return True
                else:
                    return False
            if idx == len(arr[0]):
                tmp = 0
                for t in arr[pos][:-1]:
                    tmp += lookup[t]
                tmp += carry
                a, b = divmod(tmp, 10)
                if b != lookup[arr[pos][-1]]: return False
                return dfs(pos + 1, 0, a)


a = Solution()
print(a.isSolvable2(words=["SEND", "MORE"], result="MONEY"))
# print(a.isSolvable(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY"))
# print(a.isSolvable(words=["THIS", "IS", "TOO"], result="FUNNY"))
# print(a.isSolvable(words=["LEET", "CODE"], result="POINT"))
# print(a.isSolvable(["THAT","IS","WHY","IT","IS"],"FALSE"))
# print(a.isSolvable(["JACAH","IIJI","GACG"], "DDJF"))
# print(a.isSolvable(["CHE","IJGD","GFJG","GAD","GCG"],"EEIE"))
