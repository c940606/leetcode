class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':

        even_sum = sum([i for i in A if i % 2 == 0])
        res = []
        for val, idx in queries:
            if A[idx] % 2 == 0:
                if val % 2 == 0:
                    even_sum += val
                    A[idx] += val
                    res.append(even_sum)
                else:
                    even_sum -= A[idx]
                    A[idx] += val
                    res.append(even_sum)
            else:
                if val % 2 == 0:
                    A[idx] += val
                    res.append(even_sum)
                else:
                    A[idx] += val
                    even_sum += A[idx]
                    res.append(even_sum)
        return res


a = Solution()

print(a.sumEvenAfterQueries(A=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]))
