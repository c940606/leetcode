class Solution(object):
	def validateStackSequences(self, pushed, popped):
		"""
		:type pushed: List[int]
		:type popped: List[int]
		:rtype: bool
		"""
		i = 0
		j = 0
		stack = []
		n = len(pushed)
		# stack.append(pushed[i])
		# i += 1

		while  i < n or stack:
			print(stack)
			if not stack:
				stack.append(pushed[i])
				i += 1
			elif i >= n and stack[-1] != popped[j]:
				print(stack[-1],j)
				return False
			elif stack[-1] != popped[j]:
				stack.append(pushed[i])
				i += 1
			elif stack[-1] == popped[j]:
				j += 1
				stack.pop()
		return True
a = Solution()
print(a.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
print(a.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
print(a.validateStackSequences([4,0,1,2,3],[4,2,3,0,1]))
