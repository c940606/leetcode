def longestCommonPrefix(strs):
    '''
    输入: ["flower","flow","flight"]
    输出: "fl"
    -------------------------------------
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    :param strs:
    :return:
    '''
    s = ""
    i = 0
    while i < len(strs[0]):
        for item in strs[1:]:
            if not item.startswith(strs[0][0:i + 1]):
                return s
        s += strs[0][i]
        i += 1
    return strs[0]


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        i = 0
        if not strs:
            return s
        while i < len(strs[0]):
            for item in strs[1:]:
                if not item.startswith(strs[0][0:i + 1]):
                    return s
            s += strs[0][i]
            i += 1
        return strs[0]

    def longestCommonPrefix1(self, strs):
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp_set.pop()
        return res



str1 = ["flo", "flower", "flow", "floight"]
str2 = ["dog", "racecar", "car"]
a = Solution()
print(a.longestCommonPrefix1(str1))
