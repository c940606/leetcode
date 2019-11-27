class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        phrases_split = [phrase.split() for phrase in phrases]
        #print(phrases_split)
        res = set()
        n = len(phrases)
        for i in range(n):
            for j in range(i + 1, n):
                if phrases_split[i][0] == phrases_split[j][-1]:
                    res.add(" ".join(phrases_split[j] + phrases_split[i][1:]))
                if phrases_split[i][-1] == phrases_split[j][0]:
                    res.add(" ".join(phrases_split[i] + phrases_split[j][1:]))
        return sorted(res)


a = Solution()
print(a.beforeAndAfterPuzzles(["writing code", "code rocks"]))
print(a.beforeAndAfterPuzzles(phrases=["mission statement",
                                       "a quick bite to eat",
                                       "a chip off the old block",
                                       "chocolate bar",
                                       "mission impossible",
                                       "a man on a mission",
                                       "block party",
                                       "eat my words",
                                       "bar of soap"]))
