class Solution(object):
	def distinctSubseqII(self, S):
		"""
		给定一个字符串 S，计算 S 的不同非空子序列的个数。
		因为结果可能很大，所以返回答案模 10^9 + 7.
		--
		输入："abc"
		输出：7
		解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
		:type S: str
		:rtype: int
		"""
		if not S:
			return 0
		res =[]
		def helper(S,temp):
			if temp:
				res.append(temp)
			for i in range(len(S)):
				helper(S[i+1:],temp+S[i])
		helper(S,"")
		return len(res)

	def distinctSubseqII1(self, S):
		if not S:
			return 0
		n = len(S)
		mod = 1000000007
		res = [1]+[0]*(n-1)
		visited = {S[0]}
		i = 1
		sum = res[0]
		while i < n:
			j = 0
			while j < i+1 :
				# print(res)
				temp = S[:j+1]+S[i]
				if i==j :
					if S[i] not in visited:
						# print(S[i])
						res[i] += 1
						visited.add(S[i])
				elif temp not in visited:
					# print(S[:j+1]+S[i])
					res[i] += res[j]
					visited.add(temp)
				j += 1
			sum += res[i]
			i += 1
		return sum%mod
a = Solution()
print(a.distinctSubseqII1("abc"))
print(a.distinctSubseqII1("aaa"))
print(a.distinctSubseqII1("lee"))
print(a.distinctSubseqII1("aba"))
print(a.distinctSubseqII1("pcrdhwdxmqdznbenhwjsenjhvulyve"))
print(a.distinctSubseqII1("dzekfwoerewfdfetqeteripdsafdsafdfadkljkdjfioewiokljdfjkliouerjklklafjziioeqfkljakldfioupiouipuiuipupopkdfkmcmxvajdfkjqjefkklmdsafmcmvcmzxkorkpsuvmjxjdfadfadsfdasgadfdsfjkjsdkjfkjadskjkfjalskflkdfkjkdfkjkadskfaksdjfkcvzxm,cvmaqyrhpkfpadafdfadsfadgfdhthjkjdafjdiojfoeqrkdjaoifjewnflkncvondklvnlkvkadjvadafdfdafdiaaloqxyeptyijjukpkxhivdompbonazxoifnobxhewujsabzqqpyzaboapiayulhbyspjkbsqdrnfavsgrvoiadjgnnangmkbqkcfhwqdazwczdpgqvrbsiivjcfkzduimiuulttistvtoatznfqndevafbjkwbxqsbdmvmmyuknktiuiimplaxmqitufntzzodptqfintaboshpkpwcytvtbemxmjyjkgbeqpfiokqfewwosjceiyklwfqvvxobwgrdkhezqyqhfipznvcytywhuskuhzjwgyfxwhcjgyvmorgmxfbaqrilojawyersuxjyybdwwnalubvxtdgupruojrenjwntkymvlavxqzcelhnmyupfeomuxpnyjddiaezmlqteowzblmwegckaplwjpotqdttohtstxqshkmphassfqnecrzowwsotdsbjjghkaadocrsyilxbltwwxhjcgqrednafwzdwdiygkkdijnxmrvmlqcnnyvmrjrugbrhbyzzvnnhswsqubqlbyiresjewdbxowmvvkycizocgwbsjnydznwwxhazmbrtnhfetsaztvolonecfelglmskktaynfxouykntmjgnqbxlwhimutlouevxuescberkqlfrsobutbgivgnyhmcwrsytfqmgrnsqhlxtlucjuzoybflnkvtbfaqrupfxkfrjofvoghseyrndsaiqclrazinkkxivucgfeosrpgmwmzsowjfhaepuukutkavldvvqvpplvttpoltirexcsmgrakdthbutzdlkmbenbekpxitcohldhkxsdethhqrxyetrjaaowenaegoqgonpxzngvwjqvqfdqzqdxttfafgtpemnvkarsewyiyqdvhdiwdlvzvlyxathpeaepiwsfkcayriquikfjaivyrqltvvezgyugagdufdfjxnnjjlvafawstzdhxqu"))
