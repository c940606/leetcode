class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nxt_num = {}
        mda = []  # monotonicallyDecreasingArray

        for n2 in nums2:
            while mda and mda[-1] < n2:
                nxt_num[mda.pop()] = n2
            mda.append(n2)
        res = []
        for n2 in nums1:
            res.append(nxt_num.get(n2, -1))
        return res
