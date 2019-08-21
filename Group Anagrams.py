class Solution:
    def groupAnagrams(self, strs):
        """
        给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
        ----
        输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
        输出:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lookup = {}
        # print(strs)
        for item in strs:
            # print(item)
            print(sorted(item))
            temp = "".join(sorted(item))
            print(temp)
            if temp in lookup:
                lookup[temp] += [item]
            else:
                lookup[temp] = [item]
        return list(lookup.values())

    def groupAnagrams1(self, strs):
        from collections import defaultdict
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        lookup = defaultdict(list)
        for _str in strs:
            key_val = 1
            for s in _str:
                key_val *= prime[ord(s) - 97]
            lookup[key_val].append(_str)
        return list(lookup.values())


a = Solution()
str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(a.groupAnagrams(str1))
