class Solution:
    def shipWithinDays(self, weights, D):
        n = len(weights)
        def helper(i, D, res_list):
            if D == 1:
                return max(max(res_list), sum(weights[i:]))
            res = sum(weights)
            for j in range(i + 1, n):
                res = min(res, helper(j, D - 1, res_list + [sum(weights[i:j])]))
            return res
        t = helper(0, D, [])
        return t

    def shipWithinDays1(self, weights, D):
        sum_weights = sum(weights)
        if D == 1:
            return sum(weights)
        if len(weights) == D:
            return max(weights)
        #print(sum_weights)
        n = len(weights)
        # print(sum_weights // D)
        def helper(t,D):
            res = [0]*(D)
            i = 0
            for weight in weights:
                res[i] += weight
                if i < D-1 and res[i] > t:
                    res[i] -= weight
                    i += 1
                    res[i] += weight
            # print(res)
            if res[-1] < t:
                return True
            else:
                return False
        left = sum_weights // D
        right = sum_weights
        while left < right:
            mid = (left + right) // 2
            #print(left,right,mid)
            if helper(mid,D):
                right = mid
            else:
                left = mid+1
            #break
        return left

    def shipWithinDays2(self, weights, D):
        import  math
        left = math.ceil(sum(weights)/ D)
        right = sum(weights)
        while left <right:
            mid = left + (right - left)//2
            need_day = 1
            cur = 0
            for weight in weights:
                if cur + weight> mid:
                    need_day += 1
                    cur = 0
                cur += weight
            if need_day > D:
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
print(a.shipWithinDays2(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D=5))
#print(a.shipWithinDays1(weights = [3,2,2,4,1,4], D = 3))
#print(a.shipWithinDays1([180,373,75,82,497,23,303,299,53,426,152,314,206,433,283,370,179,254,265,431,453,17,189,224],12))
