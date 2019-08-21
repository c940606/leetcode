class Solution(object):
    def wordBreak2(self, s, wordDict):
        """
        给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
        说明：
            拆分时可以重复使用字典中的单词。
            你可以假设字典中没有重复的单词。
        ---
        输入: s = "leetcode", wordDict = ["leet", "code"]
        输出: true
        解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
        ---
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True

        for i in range(n):
            if s[:i + 1] in wordDict:
                print(s)
                if self.wordBreak(s[i + 1:], wordDict):
                    return True
            # else:
            # 	return False
        return False

    def wordBreak1(self, s, wordDict):
        n = len(s)
        flg = [False] * n
        for i in range(n):
            for item in wordDict:
                l = len(item)
                if s[i - l + 1:i + 1] == item and (flg[i - l] or i - l == -1):
                    flg[i] = True
        return flg[-1]

    def wordBreak(self, s, wordDict):
        n = len(s)
        if not wordDict: return not s
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


a = Solution()
# s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
w = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(a.wordBreak1(s, w))
