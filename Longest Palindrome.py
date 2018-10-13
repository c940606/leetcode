from collections import Counter


class Solution(object):
	def longestPalindrome(self, s):
		"""
		给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
		在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
		注意:
		假设字符串的长度不会超过 1010。
		---
		输入:
		"abccccdd"
		输出:
		7
		解释:
		我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
		---

		:type s: str
		:rtype: int
		"""
		lookup = Counter(s)
		print(lookup)
		odd= []
		even = []

		for num in lookup.values():
			if num % 2 == 0:
				even.append(num)
			else:
				odd.append(num)
		print(odd,even)
		if not odd :
			return sum(even)


		return sum(odd) - (len(odd)-1)+sum(even)


a = Solution()
# print(a.longestPalindrome("abccccdd"))
print(a.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
print(a.longestPalindrome("bb"))