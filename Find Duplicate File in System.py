class Solution(object):
	def findDuplicate(self, paths):
		"""
		给定一个目录信息列表，包括目录路径，以及该目录中的所有包含内容的文件，您需要找到文件系统中的所有重复文件组的路径。一组重复的文件至少包括二个具有完全相同内容的文件。
		输入列表中的单个目录信息字符串的格式如下：
		"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
		这意味着n档案（f1.txt, f2.txt ... fn.txt 有内容 f1_content, f2_content ... fn_content（分别）在目录 root/d1/d2/.../dm 中注意，n>=1 和 m>=0。如果 m=0，则表示该目录只是根目录。
		该输出是重复文件路径组的列表。对于每个组，它包含具有相同内容的文件的所有文件路径。文件路径是具有下列格式的字符串：
		"directory_path/file_name.txt"
		---
		输入：
		["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
		输出：
		[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
		:type paths: List[str]
		:rtype: List[List[str]]
		"""
		if not paths:
			return []
		lookup = {}
		for path in paths:
			temp = path.split()
			for file in temp[1:]:
				loc = file.index("(")
				file_name = file[loc+1:-1]
				if file_name in lookup:
					lookup[file_name].append(temp[0]+"/"+file[:loc])
				else:
					lookup[file_name] = [temp[0]+"/"+file[:loc]]
		# res = []
		# for value in lookup.values():
		# 	if len(value)>1:
		# 		res.append(value)
		return [i for i in lookup.values() if len(i)>1]
a = Solution()
print(a.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
print(a.findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]))
