from collections import Counter


class Solution(object):
	def isNStraightHand(self, hand, W):
		"""
		爱丽丝有一手（hand）由整数数组给定的牌。
		现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。
		如果她可以完成分组就返回 true，否则返回 false。
		---
		输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
		输出：true
		解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
		---
		输入：hand = [1,2,3,4,5], W = 4
		输出：false
		解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。
		---
		提示：
		1 <= hand.length <= 10000
		0 <= hand[i] <= 10^9
		1 <= W <= hand.length
		:type hand: List[int]
		:type W: int
		:rtype: bool
		"""

		n = len(hand)
		if n % W != 0:
			return False
		print("---")
		c = Counter(hand)
		print(c[10])
		print(c)
		for i in sorted(c):
			print(i)
			if c[i] > 0:
				for j in range(W - 1, -1, -1):
					c[i + j] -= c[i]
					if c[i + j] < 0:
						return False
		return True


a = Solution()
print(a.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3))
# print(a.isNStraightHand(hand = [1,2,3,4,5], W = 4))
