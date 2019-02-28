class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.lookup = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        t = self.lookup
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t["#"] = "#"

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.lookup
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if "#" in t:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.lookup
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


trie = Trie()
trie.insert("apple")
print(trie.lookup)
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))