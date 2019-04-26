class Solution:
    def findSubstring(self, s: str, words):
        from  collections import Counter
        if not s or not words:
            return []
        c = Counter(words)
        nums = len(words)
        nums_len = len(words[0])
        all_len = nums * nums_len
        res = []

        def helper(tmp):
            copy_words = c.copy()
            for j in range(0, all_len, nums_len):
                t = tmp[j:j + nums_len]
                # print(t)
                if t in copy_words and copy_words[t] > 0:
                    copy_words[t] -= 1
                else:
                    return False
            return True

        for i in range(0, len(s) - all_len + 1):
            tmp_s = s[i:i + all_len]
            # print(tmp_s)
            if helper(tmp_s):
                res.append(i)
        return res

    def findSubstring1(self, s: str, words):
        from collections import Counter
        if not s or not words:
            return []
        c = Counter(words)
        word_len = len(words[0])
        all_len = word_len * len(words)
        res = []
        for i in range(0, len(s) - all_len + 1):
            tmp = s[i:i + all_len]
            t = Counter()
            for j in range(0, all_len, word_len):
                t[tmp[j:j + word_len]] += 1
            if t == c:
                res.append(i)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(a.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
    print(a.findSubstring("ababaab", ["ab", "ba", "ba"]))
