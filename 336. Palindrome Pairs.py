from typing import List
from functools  import lru_cache

class Solution:
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
        lookup = {}
        palid_list = []

        def helper(tmp1, tmp2, flag=True):
            if flag:
                loc = tmp2.find(tmp1[::-1])
                if loc == 0:
                    tmp = tmp2[len(tmp1):]
                    # print(tmp)
                    if tmp and tmp in lookup:
                        return lookup[tmp]
                return -1
            else:
                tmp2 = tmp2[::-1]
                loc = tmp2.find(tmp1)
                # print(tmp1, tmp2, loc)
                if loc == 0:
                    tmp = tmp2[len(tmp1):]
                    # print(tmp)
                    if tmp and tmp[::-1] in lookup:
                        return lookup[tmp[::-1]]
                return -1

        for idx, word in enumerate(words):
            lookup[word[::-1]] = idx
            if word == word[::-1]:
                palid_list.append(idx)
        # print(lookup)
        res = []
        for idx, word in enumerate(words):
            # 找整体都是回文的
            if word in lookup and lookup[word] != idx:
                res.append([lookup[word], idx])
                # res.append([idx, lookup[word]])
            mid = (len(word) - 1) // 2
            # print(mid)
            if mid == -1:
                for j in palid_list:
                    if j != idx:
                        res.append([idx, j])
                        res.append([j, idx])
            # 右半边
            for i in range(0, mid + 1):
                # [look , idx]
                # 奇数
                word_loc = helper(word[:i], word[i + 1:])
                # print(word_loc)
                if word_loc != -1:
                    # print(1)

                    res.append([word_loc, idx])
                # 偶数
                if i != mid and word[i] == word[i + 1]:
                    # print(66)
                    word_loc = helper(word[:i], word[i + 2:])
                    # print(word_loc)
                    if word_loc != -1:
                        # print(2)
                        res.append([word_loc, idx])
            for i in range(mid + 1, len(word)):
                # [idx, look]
                # print("i", i)
                word_loc = helper(word[i + 1:], word[: i], False)
                if word_loc != -1:
                    print(3, i, word[i + 1:], word[: i])
                    res.append([idx, word_loc])
                if word[i] == word[i - 1]:
                    # print(77,word[i:], word[:i - 1])
                    word_loc = helper(word[i + 1:], word[:i - 1], False)
                    if word_loc != -1:
                        print(4)
                        res.append([idx, word_loc])
            # break
        return res

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        1. 哈希
        :param words:
        :return:
        """
        # 本身就是回文串单词
        palidStr = []
        # 翻转单词记录位置
        rev_words = {}
        # 结果
        res = []
        for idx, word in enumerate(words):
            rev_words[word[::-1]] = idx
            # 为了防止数组里有空字符串("")
            if word == word[::-1]:
                palidStr.append(idx)
        for idx, word in enumerate(words):
            if word:
                # 这里没有 len(word) + 1
                for i in range(len(word)):
                    left, right = word[:i], word[i:]
                    # 是否存在在单词左边加 使得成为回文串
                    if left == left[::-1] and right in rev_words and idx != rev_words[right]:
                        res.append([rev_words[right], idx])
                    # 同理
                    if right == right[::-1] and left in rev_words and idx != rev_words[left]:
                        res.append([idx, rev_words[left]])
            else:
                # 对于空字符串
                for loc in palidStr:
                    if loc != idx:
                        res.append([idx, loc])
        return res


a = Solution()
print(a.palindromePairs(["a", "bacaba"]))
print(a.palindromePairs(["afdafd", "a"]))
print(a.palindromePairs(["a", ""]))
print(a.palindromePairs(["", "a"]))
print(a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(a.palindromePairs(["lls", "sssll"]))
print(a.palindromePairs(["cd", "dcbab"]))
print(a.palindromePairs(["bat", "tab", "cat"]))
print(a.palindromePairs(["a", "", "aba"]))
print(a.palindromePairs(["aa", "a", "aaa"]))
print(a.palindromePairs(["aaa", "a"]))
print(a.palindromePairs(["a", "caba"]))
["bb", "bababab", "baab", "abaabaa", "aaba", "", "bbaa", "aba", "baa", "b"]
print(a.palindromePairs(["abaabaa", "baab"]))
print(a.palindromePairs(["bb", "bababab", "baab", "abaabaa", "aaba", "", "bbaa", "aba", "baa", "b"]))
# print(a.palindromePairs(["aaba", "b"]))
# print(sorted([[9,0],[0,9],[0,5],[5,1],[8,2],[2,5],[4,3],[7,4],[4,8],[0,5],[1,5],[2,5],[7,5],[9,5],[6,0],[5,7],[8,9],[5,9]]))
# print(sorted(
#     [[0, 5], [0, 9], [9, 0], [5, 0], [1, 5], [5, 1], [2, 5], [8, 2], [5, 2], [4, 3], [7, 4], [4, 8], [6, 0], [7, 5],
#      [5, 7], [8, 9], [9, 5], [5, 9]]))
