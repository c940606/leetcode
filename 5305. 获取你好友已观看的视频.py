from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        from collections import defaultdict
        lookup = defaultdict(int)
        visited = set([id])
        arr = [id]
        while level:
            nxt = []
            for a in arr:
                for b in friends[a]:
                    if b not in visited:
                        nxt.append(b)
                        visited.add(b)
            arr = nxt
            level -= 1
        print(arr)
        for a in arr:
            for b in watchedVideos[a]:
                lookup[b] += 1
        return [a for a, b in sorted(lookup.items(), key=lambda x: (x[1], x[0]))]


a = Solution()
# print(a.watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
#                                friends=[[1, 2], [0, 3], [0, 3], [1, 2]], id=0, level=1))
# print(a.watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
#                                friends=[[1, 2], [0, 3], [0, 3], [1, 2]], id=0, level=2))
print(a.watchedVideosByFriends([["m"],["xaqhyop","lhvh"]],[[1],[0]],1,1))
