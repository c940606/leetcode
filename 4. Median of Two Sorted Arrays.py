class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        l = 0
        r = n1
        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            print("m1,m2",m1,m2)
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k - m1
        print(m1,m2)
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) * 0.5


a = Solution()
# print(a.findMedianSortedArrays([1, 3], [2]))
print(a.findMedianSortedArrays([-1, 1, 3], [2, 4, 6, 8]))
# print(a.findMedianSortedArrays([2, 4, 6, 8, 10, 12, 14,16],[-1, 1, 3, 5, 7, 9]))
