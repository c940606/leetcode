from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []

class Solution:
    def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        s = ""
        products.sort()
        for i in range(len(searchWord)):
            tmp = []
            s += searchWord[i]
            for t in products:
                if len(tmp) < 3 and t[0] == s[0] and t.startswith(s):
                    tmp.append(t)
            res.append(tmp)
        return res

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        def insert(word):
            cur = root
            for w in word:
                cur = cur.children[w]
                if len(cur.words) < 3:
                    cur.words.append(word)

        for product in products:
            insert(product)
        res = []
        cur = root
        for a in searchWord:
            if not cur or not cur.children[a]:
                cur = None
                res.append([])
            else:
                cur = cur.children[a]
                res.append(cur.words)
        return res




a = Solution()
print(a.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))
print(a.suggestedProducts(products = ["havana"], searchWord = "havana"))
print(a.suggestedProducts(products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"))
print(a.suggestedProducts(products = ["havana"], searchWord = "tatiana"))
