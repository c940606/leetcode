from pprint import pprint


class Solution:
    def wordPatternMatch1(self, pattern: str, s: str) -> bool:
        def helper(p, s, lookup1, lookup2):
            # print(p, s, lookup1, lookup2)
            if not s and not p:
                return True
            if not p or len(p) > len(s): return False
            for i in range(1, len(s) + 1):
                tmp = s[:i]
                # print(p, tmp)
                if p[0] in lookup1 and lookup1[p[0]] == tmp and tmp in lookup2 and lookup2[tmp] == p[0]:
                    if helper(p[1:], s[i:], lookup1, lookup2):
                        return True
                if p[0] not in lookup1:
                    if tmp in lookup2: continue
                    lookup1[p[0]] = tmp
                    lookup2[tmp] = p[0]
                    if helper(p[1:], s[i:], lookup1, lookup2):
                        return True
                    # if p[0] in lookup1:
                    lookup1.pop(p[0])
                    # if tmp in lookup2:
                    lookup2.pop(tmp)
            return False

        return helper(pattern, s, {}, {})

    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def helper(p, s,  p_list, s_list):
            # print(p,s, p_list, s_list)
            if not p and not s: return True
            if not p or len(p) > len(s): return False
            for i in range(1, len(s) + 1):
                p_list.append(p[0])
                s_list.append(s[:i])

                if len(set(p_list)) == len(set(s_list)) == len(set(zip(p_list, s_list))) and len(p_list) == len(s_list):
                    if helper(p[1:], s[i:], p_list, s_list):
                        return True
                p_list.pop()
                s_list.pop()
            return False
        return helper(pattern, s, [], [])


a = Solution()
print(a.wordPatternMatch("ab", "ac"))
# print(a.wordPatternMatch("abab", "redblueredblue"))
# print(a.wordPatternMatch("aabb", "xyzabcxzyabc"))
# print(a.wordPatternMatch("aaaa", "asdasdasdasd"))
# print(a.wordPatternMatch("itwasthebestoftimes", "ittwaastthhebesttoofttimes"))
# print(a.wordPatternMatch("aba", "aaaa"))
# print(a.wordPatternMatch("ba", "aaa"))
# print(a.wordPatternMatch("bestoftimes", " besttoofttimes"))
# print(a.wordPatternMatch("t0t", "tt00tt"))
#