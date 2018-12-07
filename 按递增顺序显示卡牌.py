class Solution(object):
	def deckRevealedIncreasing(self, deck):
		"""
		:type deck: List[int]
		:rtype: List[int]
		"""
		deck.sort(reverse = True)
		res = []
		for num in deck :
			if res :
				res = [res.pop()] + res
				res = [num] + res
			else:
				res.append(num)
		return res

	def deckRevealedIncreasing1(self, deck):
		from collections  import deque
		deque = deque()
		deck.sort(reverse=True)
		for num in deck:
			if deque:
				deque.appendleft(deque.pop())
				deque.appendleft(num)
			else:
				deque.appendleft(num)
		return list(deque)
a = Solution()
print(a.deckRevealedIncreasing1([17,13,11,2,3,5,7]))