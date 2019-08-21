from collections import defaultdict, Counter
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        users = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            users[u].append(w)
        lookup = Counter()
        for web in users.values():
            tmp_user = Counter()
            for i, j, k in combinations(web, 3):
                if (i, j, k) not in tmp_user:
                    tmp_user[(i, j, k)] = 1
            lookup += tmp_user
        return sorted(lookup.items(), key=lambda x: (-x[1], x[0]))[0][0]


a = Solution()
print(a.mostVisitedPattern(username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
                           timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about",
                                    "career"]
                           ))
print(a.mostVisitedPattern(["u1", "u1", "u1", "u2", "u2", "u2"],
                           [1, 2, 3, 4, 5, 6],
                           ["a", "b", "c", "a", "b", "a"]))
print(a.mostVisitedPattern(["dowg", "dowg", "dowg"],
                           [158931262, 562600350, 148438945],
                           ["y", "loedo", "y"])),
