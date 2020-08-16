class Solution:
	def patternMatching(self, pattern: str, value: str) -> bool:
		p_len, v_len = len(pattern), len(value)
		lookup = {}
		v = {}
		def dfs(i, j):
			if i == p_len and j == v_len: return True
			if i >= p_len: return False
			for k in range(j, v_len + 1):
				tmp_v = value[j:k]
				if pattern[i] in lookup and lookup[pattern[i]] == tmp_v:
					return dfs(i + 1, j + len(tmp_v))
				if tmp_v not in v and pattern[i] not in lookup:
					lookup[pattern[i]] = tmp_v
					v[tmp_v] = pattern[i]
					if dfs(i + 1, j + len(tmp_v)): return True
					lookup.pop(pattern[i])
					v.pop(tmp_v)
			return False

		return dfs(0, 0)

a = Solution()
print(a.patternMatching(pattern = "abba", value = "dogcatcatdog"))

print(a.patternMatching(pattern = "aaaa", value = "dogcatcatdog"))
print(a.patternMatching(pattern = "abba", value = "dogcatcatfish"))
print(a.patternMatching(pattern = "abba", value = "dogdogdogdog"))
print(a.patternMatching(pattern="ab", value=""))