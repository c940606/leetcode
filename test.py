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

s= "abccba"
s1 = "acdca"
print(longestPalindrome(s))
print(longestPalindrome(s1))
