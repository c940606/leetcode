class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        cur = set([(beginWord,)])
        n = len(beginWord)
        wordList = set(wordList)
        res = []
        flag = False
        while cur and wordList:
            if flag == True:break
            next_time = set()
            for tmp in cur:
                if tmp[-1] == endWord:
                    res.append(list(tmp))
                    flag = True
                if tmp[-1] in wordList:
                    wordList.remove(tmp[-1])
                for i in range(n):
                    for j in range(97, 123):
                        if tmp[-1][:i] + chr(j) + tmp[-1][i + 1:] in wordList:
                            next_time.add(tmp + (tmp[-1][:i] + chr(j) + tmp[-1][i + 1:],))
            cur = next_time
        return res
a = Solution()
print(a.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))