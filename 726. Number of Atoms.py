class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        from collections import defaultdict
        n = len(formula)
        i = 0
        lookup = defaultdict(int)
        stack = []
        while i < n:
            if formula[i] == "(":
                stack.append(lookup.copy())
                lookup.clear()
                i += 1
            elif formula[i] == ")":
                # print(lookup,i)
                right = i + 1
                val = 0
                while right < n and formula[right].isdigit():
                    val = val * 10 + int(formula[right])
                    right += 1
                if val == 0:
                    t_num = 1
                else:
                    t_num = val
                if stack:
                    tmp = lookup.copy()
                    lookup = stack.pop()
                    # print(lookup)
                    for k in tmp:
                        lookup[k] = lookup[k] + tmp[k] * t_num
                i = right
            else:
                right = i
                while right < n - 1 and formula[right + 1].islower():
                    right += 1
                tmp = formula[i:right + 1]
                i = right + 1

                val = 0
                while i < n and formula[i].isdigit():
                    val = val * 10 + int(formula[i])
                    i += 1
                if val == 0:
                    val = 1
                lookup[tmp] = lookup[tmp] + val
        res = ""

        for k in sorted((lookup.keys())):
            if lookup[k] != 1:
                res += k + str(lookup[k])
            else:
                res += k
        return res


a = Solution()
print(a.countOfAtoms("Saa2O32"))
print(a.countOfAtoms("Mg(OH)2"))
print(a.countOfAtoms("K4(ON(SO3)2)2"))
