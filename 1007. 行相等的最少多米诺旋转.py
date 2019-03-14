class Solution:
    def minDominoRotations(self, A, B):
        if not A:
            return -1
        cur = [A + B]
        n = len(A)
        step = 0
        visited = set()
        visited.add(tuple(A + B))
        # print(cur,visited)
        while cur:
            next_time = []
            for tmp in cur:
                # print(tmp)
                tmp_A, tmp_B = tmp[:n], tmp[n:]
                # print(tmp_A,tmp_B)
                if len(set(tmp_A)) == 1 or len(set(tmp_B)) == 1:
                    return step
                for i in range(len(tmp_A)):
                    tmp_AA = tmp_A[:]
                    tmp_BB = tmp_B[:]
                    tmp_AA[i], tmp_BB[i] = tmp_BB[i], tmp_AA[i]
                    if tuple(tmp_AA + tmp_BB) not in visited:
                        next_time.append(tmp_AA + tmp_BB)
                        visited.add(tuple(tmp_AA + tmp_BB))
            step += 1
            cur = next_time
        return -1

    def minDominoRotations1(self, A, B):
        from collections import defaultdict
        lookup_A = defaultdict(set)
        lookup_B = defaultdict(set)
        for idx, val in enumerate(A):
            lookup_A[val].add(idx)
        for idx, val in enumerate(B):
            lookup_B[val].add(idx)
        # print(lookup_A,lookup_B)
        res = len(A) + 1
        n = len(A)
        for a in lookup_A:
            tmp_n = len(lookup_A[a])
            # print(lookup_A[a],lookup_B[a])
            if len(lookup_B[a] - (lookup_A[a] & lookup_B[a])) == n - tmp_n:
                res = min(res, n - tmp_n)
        for b in lookup_B:
            tmp_n = len(lookup_B[b])
            if len(lookup_A[b] - (lookup_A[b] & lookup_B[b])) == n - tmp_n:
                res = min(res, n - tmp_n)
        return res if res != len(A) + 1 else -1


a = Solution()
print(a.minDominoRotations1(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]))
print(a.minDominoRotations1(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]))
print(a.minDominoRotations1(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2,
     2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2],
    [2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1,
     1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2]))
print(a.minDominoRotations1([1,2,1,1,1,2,2,2]
,[2,1,2,2,2,2,2,2]))
print(a.minDominoRotations1([1,2,1,1,1,2,2,2]
,[2,1,2,2,2,2,2,2]))
