import collections
from typing import List
class Solution:
    def entityParser(self, text: str) -> str:
        import  re

        lookup  = {
            "&quot;":'\\"',
            "&apos;": "\\'",
            "&amp;":"&",
            "&gt;":">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        # def helper(t):

        # res = []
        #         # for t in text.split():
        #         #     if "&quot;" in t or "&apos;" in t:
        #         #         res.append(helper(t))
        #         #
        #         #     elif t in lookup:
        #         #         if t == "&quot;":
        #         #             print(t, lookup[t])
        #         #             res.append("\\" + lookup[t])
        #         #         else:
        #         #             res.append(lookup[t])
        #         #     else:
        #         #         res.append(t)

        for k in lookup:
            # print(k, lookup[k])
            text.replace(k, lookup[k])
            text = re.sub(re.compile(k), lookup[k],text)
        return text

a = Solution()
print(a.entityParser("&amp; is an HTML entity but &ambassador; is not."))
print(a.entityParser("and I quote: &quot;...&quot;"))
print(a.entityParser("Stay home! Practice on Leetcode :)"))
print(a.entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))
print(a.entityParser("leetcode.com&frasl;problemset&frasl;all"))
print(a.entityParser("\'\"afa\"\'"))
