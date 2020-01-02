class Solution(object):
    def lengthLongestPath1(self, input):
        """
        :type input: str
        :rtype: int
        """
        if "." not in input:
            return 0
        depth_dict = {0: 0}
        max_depth = 0
        for line in input.split("\n"):
            # print(line)
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            if "." in name:
                max_depth = max(max_depth, len(name) + depth_dict[depth])
            else:
                depth_dict[depth + 1] = len(name) + depth_dict[depth] + 1
        # print(depth_dict)
        return max_depth

    def lengthLongestPath(self, _input: str) -> int:

        def helper(stack):
            ans = 0
            for s in stack:
                ans += len(s[1])
            return ans + len(stack) - 1

        s = _input.split("\n")
        # print(s)
        t = []
        for a in s:
            num = a.count("\t")
            t.append([num, a[num:]])
        stack = []
        res = 0
        for a in t:
            while stack and stack[-1][0] >= a[0]:
                stack.pop()
            stack.append(a)
            if "." in a[1]:
                # print(stack)
                res = max(res, helper(stack))

        return res


a = Solution()
print(a.lengthLongestPath1("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(a.lengthLongestPath1("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(a.lengthLongestPath(""))
