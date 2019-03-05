class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        cur = set([beginWord])
        step = 0
        wordList = set(wordList)
        while cur and  wordList:
            print(cur)
            step += 1
            next_time = set()
            if endWord in cur:
                return step
            for tmp in cur:
                if tmp in wordList:
                    wordList.remove(tmp)
                for i in range(n):
                    for j in range(97, 123):
                        if tmp[:i] + chr(j) + tmp[i + 1:] in wordList:
                            next_time.add(tmp[:i] + chr(j) + tmp[i + 1:])
            cur = next_time
        return 0


a = Solution()
print(a.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(a.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
print(a.ladderLength("a","c",["a","b","c"]))
