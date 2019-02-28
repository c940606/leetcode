class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':

        equ = []
        inequ = []
        for equation in equations:
            if "==" in equation:
                equation = equation.split("==")
                equ.append([equation[0], equation[-1]])
            else:
                equation = equation.split("!=")
                inequ.append([equation[0], equation[-1]])
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for x, y in equ:
            union(x, y)
        # print(f)
        for i, j in inequ:
            # print(find(i),find(j))
            if find(i) == find(j):
                return False
        return True


a = Solution()
print(a.equationsPossible(["a==b", "b!=a"]))
print(a.equationsPossible(["b==a", "a==b"]))
print(a.equationsPossible(["a==b", "b!=c", "c==a"]))
