class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while j < len(p):
            if j < len(p) and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                start = p
                match = i
                i += 1
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
        return all(x == "*" for x in p[j:])
