class Solution(object):
	def lengthLongestPath(self, input):
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

a = Solution()
print(a.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
