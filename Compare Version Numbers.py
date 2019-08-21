import itertools


class Solution(object):
    def compareVersion1(self, version1, version2):
        """
        比较两个版本号 version1 和 version2。
        如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
        你可以假设版本字符串非空，并且只包含数字和 . 字符。
         . 字符不代表小数点，而是用于分隔数字序列。
        例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
        ---
        输入: version1 = "0.1", version2 = "1.1"
        输出: -1
        ---
        输入: version1 = "1.0.1", version2 = "1"
        输出: 1
        ---
        输入: version1 = "7.5.2.4", version2 = "7.5.3"
        输出: -1
        ---
        思路:
        split
        依次比较
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version2 = version2.split(".")
        i = 0
        n1 = len(version1)
        n2 = len(version2)
        max_len = max(n1, n2)
        version1 = version1 + [0] * (max_len - n1)
        version2 = version2 + [0] * (max_len - n2)
        # print(version1,version2)
        while i < max_len:
            if int(version2[i]) == int(version1[i]):
                i += 1
            elif int(version2[i]) > int(version1[i]):
                return -1
            else:
                return 1
        return 0

    # print(i,j)
    # if i == n1:
    # 	return -1
    # if j == n2:
    # 	return 1
    def compareVersion(self, version1: str, version2: str) -> int:
        for x, y in itertools.zip_longest(version1.split("."), version2.split("."), fillvalue=0):
            if int(x) != int(y): return 1 if int(x) > int(y) else -1
        return 0


a = Solution()
print(a.compareVersion(version1="7.5.2.4", version2="7.5.3"))
