class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None


class Solution:
    def findMaximumXOR1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            cur = root
            for j in range(31, -1, -1):
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
            for j in range(31, -1, -1):
                tmp = num & 1 << j
                if cur.one and cur.zero:
                    if tmp:
                        cur = cur.zero
                    else:
                        cur = cur.one
                    val += 1 << j
                else:
                    if (cur.zero and tmp) or (cur.one and not tmp):
                        val += 1 << j
                    cur = cur.one or cur.zero
            res = max(res, val)
        return res

    def findMaximumXOR2(self, nums):
        res = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for num in nums:
                s.add(num & mask)
            tmp = res | (1 << i)
            for t in s:
                if tmp ^ t in s:
                    res = tmp
                    break
        return res

    def findMaximumXOR(self, nums):
        if not nums: return 0
        root = {}
        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                cur_bit = (num >> i) & 1
                cur.setdefault(cur_bit, {})
                cur = cur[cur_bit]

        # pprint(root)
        res = float("-inf")
        for num in nums:
            cur = root
            cur_max = 0
            for i in range(31, -1, -1):
                cur_bit = (num >> i) & 1
                # print(cur_bit)
                if cur_bit ^ 1 in cur:
                    cur_max += (1 << i)
                    cur = cur[cur_bit ^ 1]
                else:
                    cur = cur[cur_bit]
            res = max(res, cur_max)
        return res


a = Solution()
print(a.findMaximumXOR([3, 10, 5, 25, 2, 8]))
