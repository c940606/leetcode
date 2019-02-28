class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        s = "." * n
        def xiexian(i,j):
            res =set()
            tmp_i = i
            tmp_j = j
            while tmp_i + 1 < n and tmp_j + 1 < n:
                res.add((tmp_i+1,tmp_j+1))
                tmp_i += 1
                tmp_j += 1
            tmp_i = i
            tmp_j = j
            while tmp_i + 1 < n and tmp_j - 1 >= 0:
                res.add((tmp_i + 1, tmp_j - 1))
                tmp_i += 1
                tmp_j -= 1
            tmp_i = i
            tmp_j = j
            while tmp_i - 1 >= 0 and tmp_j + 1 < n:
                res.add((tmp_i - 1, tmp_j + 1))
                tmp_i -= 1
                tmp_j += 1
            tmp_i = i
            tmp_j = j
            while tmp_i - 1 >=0 and tmp_j - 1 >=0 :
                res.add((tmp_i - 1, tmp_j - 1))
                tmp_i -= 1
                tmp_j -= 1
            return res
        def helper(row,col,xiexian_set,tmp):
            if row == n-1 :
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and (row+1,j) not in xiexian_set:
                    helper(row+1,col+[j],xiexian_set|xiexian(row+1,j),tmp+[s[:j]+"Q"+s[j+1:]])
        for i in range(n):
            first = s[:i] + "Q" + s[i+1:]
            xiexian_set= xiexian(0,i)
            helper(0,[i],xiexian_set, [first])
        return len(res)

a = Solution()
print(a.solveNQueens(10))
