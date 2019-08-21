class Solution(object):
    def findLadders1(self, beginWord, endWord, wordList):
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
            if flag == True: break
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

    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        distance = {}
        distance[beginWord] = 0

        wordList = set(wordList)
        res = []
        # print(wordList)
        next_word_dict = defaultdict(list)

        def next_word(word):
            ans = []
            for i in range(len(word)):
                for j in range(97, 123):
                    tmp = word[:i] + chr(j) + word[i + 1:]
                    if tmp != word and tmp in wordList:
                        ans.append(tmp)
            return ans

        def bfs():
            cur = [beginWord]
            step = 0
            flag = False
            while cur:
                step += 1
                next_time = []
                for word in cur:
                    for nw in next_word(word):
                        next_word_dict[word].append(nw)
                        if nw == endWord:
                            flag = True
                        if nw not in distance:
                            distance[nw] = step
                            next_time.append(nw)
                if flag:
                    break
                cur = next_time

        def dfs(tmp, step):
            if tmp[-1] == endWord:
                res.append(tmp)
                return
            for word in next_word_dict[tmp[-1]]:
                if distance[word] == step + 1:
                    dfs(tmp + [word], step + 1)

        bfs()
        dfs([beginWord], 0)
        return res


a = Solution()
print(a.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(a.findLadders("kiss", "tusk", ["miss", "dusk", "kiss", "musk", "tusk", "diss", "disk", "sang", "ties", "muss"]))
