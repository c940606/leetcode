class Solution:
    def accountsMerge(self, accounts):
        from collections import defaultdict
        if not accounts:
            return
        lookup = defaultdict(list)
        res = []
        for account in accounts:
            name = account[0]
            email = set(account[1:])

            lookup[name].append(email)
            for e in lookup[name][:-1]:
                if e & email:
                    lookup[name].remove(e)
                    lookup[name][-1].update(e)
        for key, val in lookup.items():

            for tmp in val:
                res.append([key] + list(sorted(tmp)))
        return res

    def accountsMerge1(self, accounts):
        from collections import defaultdict

        f = {}

        def find(x):
            f.setdefault(x, x)
            while f[x] != x:
                x = f[x]
            return x

        def union(x, y):
            f[find(x)] = find(y)

        lookup = {}
        n = len(accounts)
        for idx, account in enumerate(accounts):
            name = account[0]
            email = account[1:]
            for e in email:
                if e in lookup:
                    union(idx, lookup[e])
                else:
                    lookup[e] = idx
        # print(f)
        disjointSet = defaultdict(set)
        for i in range(n):
            tmp = find(i)
            for es in accounts[i][1:]:
                disjointSet[tmp].add(es)
        # print(disjointSet)
        res = []
        for key, val in disjointSet.items():
            res.append([accounts[key][0]] + list(sorted(val)))
        return res

    def accountsMerge2(self, accounts):
        from collections import defaultdict, deque
        graph = defaultdict(set)
        email_to_name = defaultdict()
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                graph[emails[0]].add(email)
                graph[email].add(emails[0])
        # print(graph)
        visited = set()
        res = []

        def bfs(e):
            ans = []
            stack = deque()
            stack.appendleft(e)
            while stack:
                tmp = stack.pop()
                ans.append(tmp)
                for t in graph[tmp]:

                    if t not in visited:
                        visited.add(t)
                        stack.appendleft(t)
            return ans

        for e in graph:
            # print(e)
            if e not in visited:
                visited.add(e)
                ans = bfs(e)
                res.append([email_to_name[e]] + sorted(ans))
        return res

    def accountsMerge3(self, accounts):
        from collections import defaultdict, deque
        graph = defaultdict(set)
        email_to_name = defaultdict()
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                graph[emails[0]].add(email)
                graph[email].add(emails[0])
        # print(graph)
        visited = set()
        res = []
        def dfs(e):
            new_list.append(e)
            for t in graph[e]:
                if t not in visited:
                    visited.add(t)
                    dfs(t)
        for e in graph:
            if e not in visited:
                visited.add(e)
                new_list = []
                dfs(e)
                res.append([email_to_name[e]] + sorted(new_list))
        return res



a = Solution()
print(a.accountsMerge3(accounts=[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                                 ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
print(a.accountsMerge3(
    [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
     ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
     ["David", "David1@m.co", "David2@m.co"]]))
