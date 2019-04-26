class Solution:
    def numSimilarGroups(self, A):
        f = {}

        for i in range(len(A)):
            f[i] = i
        self.res = len(A)

        def find(x):
            # f.setdefault(x, x)
            p = x
            while x != f[x]:
                x = f[x]
            while x != p:
                t = f[x]
                f[x] = p
                x = t
            return x

        def union(x, y):
            tmp1 = find(x)
            tmp2 = find(y)
            if tmp1 != tmp2:
                f[tmp1] = tmp2
                self.res -= 1

        if not A:
            return 0
        n = len(A[0])

        def smilar(x, y):
            cout = 0
            for i in range(n):
                if x[i] != y[i]:
                    cout += 1
                if cout > 2:
                    return False
            return True

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                # print(A[i], A[j])
                if smilar(A[i], A[j]):
                    # print(A[i],A[j])
                    union(i, j)

        return self.res

    def numSimilarGroups1(self, A):
        res = 0
        n = len(A)
        visited = set()

        def smilar(x, y):
            cout = 0
            for i in range(len(A[0])):
                if x[i] != y[i]:
                    cout += 1
                if cout > 2:
                    return False
            return True

        def dfs(i, visited):
            for j in range(n):
                if j not in visited and smilar(A[i], A[j]):
                    visited.add(j)
                    dfs(j, visited)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                res += 1
                dfs(i, visited)
        return res

    def numSimilarGroups2(self, A):
        from collections import deque
        n = len(A)
        queue = deque()
        visited = set()
        res = 0

        def smilar(x, y):
            cout = 0
            for i in range(len(A[0])):
                if x[i] != y[i]:
                    cout += 1
                if cout > 2:
                    return False
            return True

        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue.appendleft(i)
                res += 1
                while queue:
                    tmp = queue.pop()
                    for j in range(n):
                        if j not in visited and smilar(A[tmp], A[j]):
                            visited.add(j)
                            queue.appendleft(j)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.numSimilarGroups2(["tars", "rats", "arts", "star"]))
