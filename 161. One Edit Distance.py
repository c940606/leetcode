class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t: return False
        n1 = len(s)
        n2 = len(t)
        if abs(n1 - n2) > 1: return False
        if not s or not t: return True
        if n1 > n2: return self.isOneEditDistance(t, s)
        if n1 == n2:
            i = 0
            not_same = 0
            while i < n1:
                if s[i] != t[i]:
                    not_same += 1
                if not_same > 1:
                    return False
                i += 1
            return True
        else:
            i = 0
            j = 0
            not_same = 0
            while i < n1 and j < n2:
                if s[i] != t[j]:
                    j += 1
                    not_same += 1
                if not_same > 1 : return False
                if s[i] == t[j]:
                    i += 1
                    j += 1
            #print(i,j )
            return i == n1 and (not_same + n2 - j) == 1




a = Solution()
print(a.isOneEditDistance(s="ab", t="acb"))
print(a.isOneEditDistance(s="cab", t="ad"))
# print(a.isOneEditDistance(s="1203", t="1213"))
# print(a.isOneEditDistance("", ""))
# print(a.isOneEditDistance("cb", "ab"))
# print(a.isOneEditDistance("A", "a"))
print(a.isOneEditDistance("a","ac"))
