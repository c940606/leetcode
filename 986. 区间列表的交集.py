# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        i = 0
        j = 0
        n = len(A)
        m = len(B)
        res = []
        while i < n and j < m:
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]:
                j += 1

            elif A[i][0] <= B[j][0] <= A[i][1]<= B[j][1]:
                res.append([B[j][0], A[i][1]])
                if A[i][1] < B[j][1]:
                    i += 1
                elif A[i][1] == B[j][1]:
                    i += 1
                    j += 1
            elif B[j][0] <=A[i][0] <= A[i][1]<=B[j][1]:
                res.append([A[i][0],A[i][1]])
                if A[i][1] < B[j][1]:
                    i += 1
                elif A[i][1] == B[j][1]:
                    i += 1
                    j += 1
            elif A[i][0]<=B[j][0] <=B[j][1] <=A[i][1]:
                res.append([B[j][0],B[j][1]])
                if B[j][1] < A[i][1]:
                    j += 1
                elif B[j][1] == A[i][1]:
                    i += 1
                    j += 1
            elif B[j][0] <= A[i][0] <= B[j][1] <= A[i][1]:
                res.append([A[i][0], B[j][1]])
                if B[j][1] < A[i][1]:
                    j += 1
                elif B[j][1] == A[i][1]:
                    i += 1
                    j += 1

        return res

    def intervalIntersection1(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        i = 0
        j = 0
        n = len(A)
        m = len(B)
        res = []
        while i < n and j < m:
            if A[i].end < B[j].start:
                i += 1
            elif B[j].end < A[i].start:
                j += 1

            elif A[i].start <= B[j].start <= A[i].end <= B[j].end:
                res.append(Interval(B[j].start, A[i].end))
                if A[i].end < B[j].end:
                    i += 1
                elif A[i].end == B[j].end:
                    i += 1
                    j += 1
            elif B[j].start <= A[i].start <= A[i].end <= B[j].end:
                res.append(Interval(A[i].start, A[i].end))
                if A[i].end < B[j].end:
                    i += 1
                elif A[i].end == B[j].end:
                    i += 1
                    j += 1
            elif A[i].start <= B[j].start <= B[j].end <= A[i].end:
                res.append(Interval(B[j].start, B[j].end))
                if B[j].end < A[i].end:
                    j += 1
                elif B[j].end == A[i].end:
                    i += 1
                    j += 1
            elif B[j].start <= A[i].start <= B[j].end <= A[i].end:
                res.append(Interval(A[i].start, B[j].end))
                if B[j].end < A[i].end:
                    j += 1
                elif B[j].end == A[i].end:
                    i += 1
                    j += 1
        return res
a = Solution()
print(a.intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))
print(a.intervalIntersection([[3,5],[9,20]],[[4,5],[7,10],[11,12],[14,15],[16,20]]))


