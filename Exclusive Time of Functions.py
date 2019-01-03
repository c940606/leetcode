class Solution(object):
	def exclusiveTime(self, n, logs):
		"""
		:type n: int
		:type logs: List[str]
		:rtype: List[int]
		"""
		from collections import deque
		if not logs:
			return 0
		logs = [log.split(":") for log in logs]
		num = len(logs)
		res = [0] * n
		stack = deque()
		# stack.append(logs[0])
		i = 0
		prev_time = 0
		while stack or i < num:
			idx,statue,timestamp = int(logs[i][0]),logs[i][1],int(logs[i][2])
			if statue == "start":
				if stack:
					res[stack[-1]] += timestamp - prev_time
				stack.append(idx)
				prev_time = timestamp
			else:
				tmp_idx = stack.pop()
				# print(tmp_idx)
				res[tmp_idx] += (timestamp - prev_time + 1)
				prev_time = timestamp + 1

			i += 1
		return res


a = Solution()
# print(a.exclusiveTime(n=2
# 					  , logs=
# 					  ["0:start:0",
# 					   "1:start:2",
# 					   "1:end:5",
# 					   "0:end:6"]))
print(a.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
print(a.exclusiveTime(1, ["0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"]))
print(a.exclusiveTime(3,
					  ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2", "2:end:2", "2:start:3", "2:end:3"]))
