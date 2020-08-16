def longestPalindrome(s):
	Max = 0
	left = 0
	right = 0
	n = len(s)
	for i in range(n):
		for j in range(min(i+1,n-i)):
			if s[i-j] != s[i+j]:
				break
			if 2*j+1>Max:
				Max = 2*j+1
				left = (i-j)
				right = (i+j)
		if i+1<n and s[i] == s[i+1]:
			for j in range(min(i+1,n-i-1)):
				if s[i-j] != s[i+j+1]:
					break
				if 2*(j+1) > Max:
					Max = 2*(j+1)
					left = (i-j)
					right = (i+j+1)
	return Max ,s[left:right+1]


def helper(s, p):
    s_split = s.split()
    p_split = p.split()
    ans = []
    i = 0
    while i < len(s_split):
        tmp_i = i
        j = 0
        while tmp_i < len(s_split) and j < len(p_split) and s_split[tmp_i] == p_split[j]:
            tmp_i += 1
            j += 1
        if j == len(p_split):
            for p in p_split:
                ans.append(p + "/B")
            i = tmp_i
        else:
            ans.append(s_split[i] + "/I")
            i += 1
    print(ans)
    return " ".join(ans)


print(helper("i love apple      apple", "love apple"))

# s= "abccba"
# s1 = "acdca"
# print(longestPalindrome(s))
# print(longestPalindrome(s1))
