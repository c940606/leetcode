class Solution(object):
	def validIPAddress(self, IP):
		"""
		编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。
		IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；
		同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。
		IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。
		然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。
		同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。
		说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。
		----
		输入: "172.16.254.1"
		输出: "IPv4"
		解释: 这是一个有效的 IPv4 地址, 所以返回 "IPv4"。
		---
		输入: "2001:0db8:85a3:0:0:8A2E:0370:7334"
		输出: "IPv6"
		解释: 这是一个有效的 IPv6 地址, 所以返回 "IPv6"。
		---
		输入: "256.256.256.256"
		输出: "Neither"
		解释: 这个地址既不是 IPv4 也不是 IPv6 地址。
		---8
		思路:
		首先判断是ipv4还是ipv6 通过 . :
		ipv4 4 个数
		1. 大于等于两位数的时候,第一为不能为0
		2. 必须是 0 到255之间的数
		ipv6  8个数
		1. 不够8 直接错
		2. 出现""错
		3. 长度

		:type IP: str
		:rtype: str
		"""
		if "." in IP:
			# ipv4
			ipv4 = IP.split(".")
			if len(ipv4) != 4:
				return "Neither"
			for num in ipv4:
				if (len(num) > 1 and num[0] == "0") or not num.isdigit() or (int(num) < 0) or (int(num) > 255):
					return "Neither"
			return "IPv4"
		else:
			ipv6 = IP.split(":")
			if len(ipv6) != 8:
				return "Neither"
			for num in ipv6:
				if not num or len(num) > 4 or not all(map(
						lambda x: x.lower() in "0123456789abcdef", num)):
					return "Neither"
			return "IPv6"
a = Solution()
print(a.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))

