class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None
class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            cur = root
            for j in range(31,-1,-1):
                tmp = num & 1 << j
                if tmp:
                    if not cur.one:
                        cur.one = TrieNode()
                    cur = cur.one
                else:
                    if not cur.zero:
                        cur.zero = TrieNode()
                    cur = cur.zero
        res = 0
        for num in nums:
            cur = root
            val = 0
            for j in range(31,-1,-1):
                tmp = num & 1 << j
                if cur.one and cur.zero:
                    if tmp:
                        cur = cur.zero
                    else:
                        cur = cur.one
                    val += 1 << j
                else:
                    if (cur.zero and  tmp ) or (cur.one and not tmp):
                        val += 1 << j
                    cur = cur.one or cur.zero
            res = max(res,val)
        return res

a = Solution()
print(a.findMaximumXOR([3, 10, 5, 25, 2, 8]))